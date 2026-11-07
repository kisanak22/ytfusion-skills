# Compatibility and prerequisites

The core is an Agent Skills directory: SKILL.md, references, optional scripts
and product-specific UI metadata in agents/openai.yaml. Use the host agent's own
installation/discovery rules. Core instructions do not depend on a named browser
automation implementation, hidden host state or an OpenAI API key.

An agent must have suitable file, terminal, browser or native API tools to
perform the requested HDS actions. A text-only chat can explain the procedure
without being able to execute it. Package installation alone does not grant
computer access or install HDS.

Identify the actual HDS edition from its native UI or installed distribution
metadata. Do not infer edition or permissions from an email or username.
Check selected provider availability in that installation.

This package includes no HDS engine, provider transport, credentials, account
session or copy of Private source. A recipe requiring a missing Private-only
provider cannot run unchanged on Shared. Explain the concrete missing capability
and ask for an acceptable supported recipe when needed; do not substitute it
silently or weaken edition boundaries.

Keep collection selection, source identity, credentials and browser sessions
local to the user's installation. A user's requested preparation scope does not
authorize application source changes, repository publishing or sending messages.

## Verification scope

The initial package is structurally validated and its read-only diagnostic
helper has stdlib fixture tests. A live read-only diagnostic can verify the
current installation's observable metadata and file counts. Its ID-mismatch
count compares stored IDs with folder names; zero does not prove that those IDs
follow the installed app's route normalization. Native Batch opening must follow
the [collection readback procedure](collections.md).

These checks do not establish live generation, provider quality, Claude Code
execution, another HDS edition, another OS or another device. Record those
separately when actually exercised. Use actual production results rather than
buying generation solely to label the skill "tested".

## Further reading

- [Agent Skills](https://agentskills.io/)
- [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)
