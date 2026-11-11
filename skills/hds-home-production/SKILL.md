---
name: hds-home-production
description: "Prepare and operate home-design channel production with an existing YtFusion HDS installation. Use for Master setup, channel and title libraries, visual and narration references, production collections, and resuming batches."
---

# HDS Home Production

Operate the user's existing HDS workflow. Support creating a Master, extending a
library, preparing a production wave, executing batches and reporting progress.
Do not treat this operating skill as a request to develop or update HDS itself.
Respond in the user's language.

## Pick the relevant procedure

- For help or "what can this skill do?", read
  [capabilities](references/capabilities.md). Explain available capabilities,
  useful inputs and examples. A clear task can proceed without a menu.
- For a new Master, channel setup, reference curation or more title stock, read
  [preparation](references/preparation.md).
- For Midjourney moodboard codes, see the manual setup and profile assignment
  procedure in [preparation](references/preparation.md#midjourney-moodboard-codes).
- For collection allocation, portable naming, capacity or moving work, read
  [collections](references/collections.md).
- For brief, Plan, media generation, resume or progress, read
  [production](references/production.md).
- For another agent, HDS edition, missing tools or an unavailable provider, read
  [compatibility](references/compatibility.md).

Load only the references relevant to the request.

## Start from the actual installation and current work

Identify the app root and the collection or intended new location. Reuse paths,
preferences and authorization already supplied. When present, read the applicable
repository guidance, installed HDS product principles and the collection's
preparation README, current ledger and manifests. Do not assume chat memory,
fixed machine paths, a particular Master name, or globally unique profile IDs.

If shell access is available, the bundled read-only helper can summarize paths,
edition markers and on-disk counts:

    python3 scripts/inspect_hds.py --app-root /path/to/YtFusion --collection /path/to/collection

Resolve that script path relative to this skill, regardless of the working
directory. An omitted collection follows the saved installation selection or
the native default. Invalid or missing saved selections are reported, never
silently replaced. The helper neither imports the application nor validates
native readiness. Matching Batch IDs and folder names alone does not establish
that the installed app can open them; use the native verification described in
[collections](references/collections.md) after preparing or renaming Batch. No
shell access is required when equivalent native UI inspection is available.

If the app or collection has not been identified, do useful independent work
and ask only for the missing location. A new device need not already have a
Master. Executing an existing independent collection does not require its
original Master.

## Preserve scope and identities

Use supported HDS UI, authenticated native APIs or existing library operations.
Do not invent API routes or JSON settings. Resolve the installed version's
interfaces when needed. Do not import and run the entire backend as a helper.

Creating a new collection uses HDS initialization and a new native identity.
Renaming, moving or resuming an existing collection preserves its identity.
Activation follows the existing collection-selection flow and any required
restart, after affected jobs, writers and cleanup are idle. Do not edit app
source or copy credentials to make a collection work.

Honor existing results and explicit stop targets. Preparation authorization
does not start paid generation. A production request authorizes the requested
native execution within its scope; do not request repetitive confirmations
already answered. Ask when a necessary location, provider substitution or
other material choice remains unresolved. Do not add a mandatory pilot.

## Keep work reusable

Treat channel count, languages, duration bands, Batch size, provider recipe,
storage budget and trend years as user parameters. Reuse compatible setup and
accepted title pools. Similar or identical titles may serve different channels;
each new project develops its own plan and requires result review.

Track stock using collection identity, profile ID, Batch ID and allocation ID.
Do not overwrite an existing title record just because normalized text matches.
Do not merge independently configured profiles from different collections.

Keep user Master data, media, credentials and progress outside this package.
Use a starter only when supplied or requested, preserving any local changes.
The skill provides procedure; installed HDS and the agent's available tools
perform the actions.

## Finish with evidence

Report what changed, where the result lives, completed/remaining units and the
next concrete action. Separate diagnostic file counts, native validation,
creative review and actual destination-device verification. Update the same
local ledger when one exists. Do not raise production progress for reorganizing
files, adding tests, completing setup again or waiving a pilot.
