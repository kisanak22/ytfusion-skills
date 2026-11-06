#!/usr/bin/env python3
"""Read HDS installation/collection metadata without importing or changing HDS."""
from __future__ import annotations

import argparse
import ast
from collections import Counter
import json
from pathlib import Path
import sys
import uuid


def read_object(path):
    if path.is_symlink():
        raise ValueError("symlink_metadata")
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError("invalid_object")
    return value


def edition_from_source(path):
    if path.is_symlink():
        return "unknown"
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, SyntaxError):
        return "unknown"
    values = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "EDITION"
            for target in node.targets
        ):
            try:
                values.append(ast.literal_eval(node.value))
            except (ValueError, TypeError):
                return "unknown"
    return values[0] if len(values) == 1 and values[0] in ("private", "shared") else "unknown"


def saved_selection(app_root):
    path = app_root / "user_data" / "hds_source.json"
    if not path.exists() and not path.is_symlink():
        return {"status": "default", "path": app_root / "user_data" / "hds", "expected_id": None}
    try:
        value = read_object(path)
        if type(value.get("schema")) is not int or value["schema"] != 1:
            raise ValueError("invalid_schema")
        if value == {"schema": 1, "mode": "default"}:
            return {"status": "default", "path": app_root / "user_data" / "hds", "expected_id": None}
        if set(value) != {"schema", "mode", "path", "collection_id"} or value["mode"] != "custom":
            raise ValueError("invalid_selection")
        target = Path(value["path"])
        if not target.is_absolute() or ".." in target.parts or target == Path(target.anchor):
            raise ValueError("invalid_path")
        identity = str(uuid.UUID(value["collection_id"]))
        if identity != value["collection_id"]:
            raise ValueError("invalid_identity")
        return {"status": "custom", "path": target, "expected_id": identity}
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        return {"status": "invalid", "path": None, "expected_id": None}


def directories(path):
    if not path.is_dir() or path.is_symlink():
        return []
    return sorted(
        (item for item in path.iterdir() if item.is_dir() and not item.is_symlink()),
        key=lambda item: item.name,
    )


def collection_summary(root, expected_id=None):
    result = {"path": str(root), "status": "missing", "native_readiness_checked": False}
    if root.is_symlink():
        result["status"] = "symlink_collection"
        return result
    if not root.exists():
        return result
    if not root.is_dir():
        result["status"] = "not_directory"
        return result
    try:
        marker = read_object(root / ".hds-collection.json")
        identity = str(uuid.UUID(marker["id"]))
        if identity != marker["id"]:
            raise ValueError("invalid_identity")
    except FileNotFoundError:
        result["status"] = "marker_missing"
        return result
    except (OSError, ValueError, TypeError, KeyError, AttributeError):
        result["status"] = "invalid_marker"
        return result
    if expected_id is not None and identity != expected_id:
        result["status"] = "identity_mismatch"
        return result
    result.update(status="observed", collection_id=identity)
    profiles = directories(root / "channel_profiles")
    batches = directories(root / "batch_projects")
    projects = directories(root / "single_projects")
    title_allocations = 0
    malformed = 0
    mismatched = 0
    statuses = Counter()
    for batch in batches:
        projects.extend(directories(batch / "projects"))
        try:
            data = read_object(batch / "batch.json")
            rows = data.get("rows_input")
            if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
                raise ValueError("invalid_rows")
            title_allocations += len(rows)
            mismatched += data.get("id") != batch.name
            status = data.get("status", "unknown")
            statuses[status if isinstance(status, str) else "unknown"] += 1
        except (OSError, ValueError, TypeError):
            malformed += 1
    result.update(
        profile_files=sum(
            (folder / "profile.json").is_file() and not (folder / "profile.json").is_symlink()
            for folder in profiles
        ),
        batch_folders=len(batches),
        title_allocations_observed=title_allocations,
        malformed_batch_metadata=malformed,
        batch_id_mismatches=mismatched,
        batch_statuses=dict(sorted(statuses.items())),
        project_folders=len(projects),
        plan_files=sum(
            (folder / "plan.json").is_file() and not (folder / "plan.json").is_symlink()
            for folder in projects
        ),
        narration_library_present=(root / "narrative_refs.json").is_file(),
        preparation_present=(root / "preparation").is_dir(),
        shared_present=(root / "shared").is_dir(),
    )
    return result


def inspect(app_root, collection=None):
    app_root = Path(app_root).expanduser().absolute()
    if app_root.is_symlink() or not (app_root / "src" / "app.py").is_file():
        return {"ok": False, "error": "not_a_hds_installation", "app_root": str(app_root)}
    selection = saved_selection(app_root)
    edition = edition_from_source(app_root / "src" / "distribution.py")
    result = {
        "ok": True,
        "app_root": str(app_root),
        "edition_marker": edition,
        "saved_selection_status": selection["status"],
        "diagnostic_only": True,
        "native_readiness_checked": False,
    }
    if collection is not None:
        root = Path(collection).expanduser().absolute()
        expected = None
        result["collection_source"] = "explicit"
    elif selection["path"] is not None:
        root = selection["path"]
        expected = selection["expected_id"]
        result["collection_source"] = "saved_selection" if expected else "native_default"
    else:
        result.update(ok=False, error="invalid_saved_selection", collection=None)
        return result
    result["collection"] = collection_summary(root, expected)
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app-root", type=Path, required=True)
    parser.add_argument("--collection", type=Path)
    args = parser.parse_args(argv)
    try:
        result = inspect(args.app_root, args.collection)
    except OSError as exc:
        result = {"ok": False, "error": type(exc).__name__, "diagnostic_only": True}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
