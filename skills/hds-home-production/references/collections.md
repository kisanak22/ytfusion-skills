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
        batch_projects/home_en_001_DEC_w01/

Use names agreed with the user. If global collection numbers are used, continue
them across later production-group folders instead of resetting to 001. Keep
codes short and distinguish folder labels from native IDs. Niche labels can sit
on Batch names; example codes are DEC, GRD, ARC, SML, COZ and NAT.

Do not rename an existing Batch folder as cosmetic text: its folder can be the
native Batch ID. Use a supported operation and synchronize required metadata
only while idle, preserving projects, history, results and source context.

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
