# Collections, names and portable ownership

A Master is a reusable preparation library. A production collection owns the
profiles and dependencies needed to execute its Batch. Each production
collection must resolve its references without the original Master path.

For a new device, choose the smallest relevant package:

- Create a new Master when starting a new library.
- Copy a supplied Master when its reusable setup is wanted.
- Copy one complete production collection to execute its existing stock.

Do not require every device to hold the entire Master or every production wave.
Copy files and native dependencies; do not replace them with symlinks to another
machine or to the skill installation.

## Allocation and names

Default to one channel per Batch with the requested title count. Keep a Batch
whole when splitting storage. A starting allocation is at most six Batch per
collection, separate languages and group heavier duration/image workloads
together. Adjust to measured storage capacity and the user's plan.

An optional naming convention is:

    Production 01/
      COL-001-EN-R/
        channel_profiles/home_en_001/
        batch_projects/home_en_001_dec_w01/

Use names agreed with the user. If global collection numbers are used, continue
them across later production-group folders instead of resetting to 001. Keep
codes short and distinguish display labels from native IDs. A Batch display
name may retain a niche tag such as DEC, GRD, ARC, SML, COZ or NAT while its
native key follows the installed application's rules.

## Native Batch keys and readback

Obtain new keys through native creation or the installed Batch route's actual
sanitizer. Do not substitute a generic filesystem sanitizer: HDS storage's
`canonical_storage_key` can preserve case while the app binding's
`_sanitize_project_name` lowercases it. In that installation, a display name
`home_en_001_DEC_w01` uses the native key/folder `home_en_001_dec_w01`. Inspect
the current binding instead of assuming every HDS version uses the same rule.

Do not rename an existing Batch folder as cosmetic text: its folder can be the
native Batch ID. Diagnose existing owners against their collection UUID, folder,
metadata ID and route normalization before changing anything. Use supported
operations while idle and synchronize the required metadata, manifests, title
contexts and tracking paths, preserving projects, history, results and choices.
Do not reset a Batch or weaken ownership checks to make a mismatch disappear.

After creation or an identity/path change, open the affected Batch through the
installed UI or authenticated native endpoint. A controlled endpoint check must
use the same sanitizer and admitted collection state/workflow as the installed
app; a permissive fallback reader can hide an invalid stored owner ID. Check the
returned key, profile, titles and options, and confirm that opening alone does
not rewrite the saved Batch. Keep this readback separate from generation,
artistic review and destination-device verification.

The same profile ID/name can exist in different collections with different
settings. Inside one collection it identifies a shared configuration. Combined
tracking uses collection UUID plus profile ID and Batch ID. Copied profiles do
not create YouTube channels; inspect any saved upload destination when reusing.

## Capacity and transfer

Base storage estimates on image count, the selected storage/compression recipe,
thumbnail count, retained alternatives and headroom. Distinguish measured setup
bytes from projected production size. Do not assume original provider files
are all the same size, or include final videos when the user excludes them.

    expected_bytes = content_images * observed_mean_bytes
                   + thumbnails + retained_history + setup + headroom

For Mac active collections follow HDS's APFS requirement. exFAT is for
archive/transfer under that workflow. On other platforms use the installed
version's supported storage requirements. Never format a disk as an incidental
preparation operation.

Use the existing native collection selection and restart behavior. Wait for
affected producers, writers and cleanup to finish before a transfer or switch.
Keep one active owner for each project/Batch, with actual device and path tracked
separately from collection identity.

Preserve UUIDs when moving an existing collection, use fresh native identities
for new collections, and verify local references and actual destination opening.
An on-disk count or unit test does not prove successful cross-device use.
