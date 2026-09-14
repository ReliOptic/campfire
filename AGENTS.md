# Campfire skill repository — operating contract

This repository name and skill invocation (`campfire`) are retained for backward compatibility. **The product artifact created by this skill is now called a Vista.**

Read before changes:

1. `AGENTS.md`
2. `PRODUCT_CLOSURE_GUARDRAIL.md`
3. `README.md`
4. `SKILL.md`

## Canonical Campsite semantics — 2026-09-14

- Camp = project/context container
- Tent = conversation thread
- Vista = interactive visual artifact
- Campfire = personalized Vista feed
- Trail = verified publisher/channel
- Stream = realtime talk + show surface
- Interactive Model = realtime capability powering Stream; not durable/product authority

Therefore:

- Do not describe the output artifact as a Campfire in new product copy/specs.
- The `campfire` skill/repo may continue to exist as a compatibility package that **composes Vista render bundles**.
- Legacy `motion_brief`/BriefEnvelope field names remain wire compatibility unless the owning Campsite schema is migrated.
- Do not rename wire fields merely to satisfy product vocabulary.

## Scope

This repository owns **Vista composition craft and compatibility output**, not Campsite feed/publishing/runtime authority.

It may produce:

- interactive HTML/SVG render bundles,
- compatible structured motion/scene payloads,
- self-check/quality evidence.

It does not own:

- Campfire personalization/ranking,
- Trail publisher verification/publication state,
- Camp/Tent persistence,
- Stream transport/session authority,
- Campsite authentication/permissions.

## Quality

Preserve the core ambition:

- advertising-grade visual craft,
- BI/data-journalism-grade factual integrity,
- interaction that deepens understanding rather than decorating text,
- domain-native art direction rather than one universal template,
- source/uncertainty/units/baseline/date honesty where relevant.

Do not regress to generic cards, fixed 8–20 second timing, or paragraph fade/slide as the default visual grammar merely because older compatibility formats contain those assumptions.

## Completion discipline

A generated file can be visually complete while the host product remains incomplete. Do not claim Campsite publish/feed/persistence/auth behavior from this skill's output alone.

If the skill claims that a Vista interaction works, verify its local interaction contract. If the task claims end-to-end Campsite behavior, that must be proven in the owning Campsite repository under its product closure guardrail.
