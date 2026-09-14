---
name: campfire
description: 원문 또는 구조화 스냅샷을 audience-of-one Vista(인터랙티브 시각 artifact)로 구성한다. `campfire`는 legacy skill invocation이며, 제품에서 Campfire는 personalized Vista feed를 뜻한다.
---

# Skill: Vista composer — legacy invocation `campfire`
# Canon: campsite-model/2026-09-14-v1

## 0. Terminology — non-negotiable

This skill keeps the invocation/package name `campfire` for compatibility. **Its output product object is a Vista.**

```text
Camp      = project/context container
Tent      = conversation thread
Vista     = interactive visual artifact      <- this skill composes this
Campfire  = personalized Vista feed          <- host product concern
Trail     = verified publisher/channel       <- host product concern
Stream    = realtime talk + show              <- host product concern
```

Never call a newly created artifact a Campfire in product-facing copy. Existing wire/schema names remain compatible until the owning Campsite schema migrates.

## 1. Job

**Lower cognitive load without lowering information density or truth. Build a scene in which understanding happens.**

The viewer should be able to explain, in their own words:

1. what changed or matters,
2. why that conclusion is supported,
3. what action, decision, uncertainty, or no-action follows.

NOT:
- slide decorator,
- dashboard reel,
- log/chain-of-thought printer,
- generic card stack,
- paragraph fade/slide sequence,
- fabricated cinematic spectacle.

ARE:
- audience-of-one information design,
- advertising-grade art direction,
- BI/data-journalism-grade factual fidelity,
- interactive visual explanation.

## 2. Inputs

You may receive:

1. **Domain pack** — domain class, slots, evidence requirements, terminology, preferred objects, action templates.
2. **Run snapshot** — authoritative values/facts for this run.
3. Optional **source material** — immutable or citable material to preserve.
4. Optional **audience context** — only what is allowed for personalization.

Rules:

- Snapshot/source facts beat stylistic priors.
- Never invent a missing number, source, date, unit, baseline, or certainty.
- If pack and snapshot disagree on a measured value, use the authoritative snapshot and surface the mismatch if material.
- Personalization may change explanation order/depth and relevance, not factual conclusion.

## 3. Authority order

1. Factual/source integrity
2. Understanding objective
3. Interaction/state correctness
4. This Vista composition contract
5. Legacy transport/schema compatibility
6. Visual polish

Visual polish is required, but never compensates for a broken state or false claim.

## 4. Understanding objective

Before scene design, complete:

> **After this Vista, the viewer can explain ________.**

Then identify:

- central tension/question,
- minimum evidence needed,
- counterexample/uncertainty if material,
- user decision/action/no-action,
- what can be explored interactively without breaking the base narrative.

If this objective cannot be stated, do not start decorating screens.

## 5. Scene grammar

### 5.1 Persistent objects over slide replacement

Prefer the same semantic object continuing across time while its relation, position, scale, state, or annotation changes.

Good:
- two teams remain identifiable while their point gap changes,
- one system diagram accumulates causality/evidence,
- one price/threshold object moves through scenarios,
- one map/flow changes under a user-controlled assumption.

Bad:
- title card disappears,
- another text card appears,
- same fact restated with a new icon,
- animation exists only as entrance/exit decoration.

### 5.2 No fixed scene count or duration

Do **not** force a universal 3–6 scene or 8–20 second template.

Timing follows:

- reading time,
- information gain,
- relation complexity,
- interaction opportunity,
- necessary holds for comprehension.

A short quiet Vista may be seconds. A complex explanation may be longer. Do not delete evidence merely to hit a duration target.

### 5.3 Motion is semantic

Motion should do at least one job:

- direct attention,
- reveal a relationship,
- show change over time/state,
- preserve continuity between explanations,
- express a user manipulation and its consequence.

Any CSS/SVG/Canvas/WebGL technique is allowed when justified and truthful. There is no universal six-property motion allowlist.

## 6. Rendering model

Preferred implementation:

- HTML/CSS/JavaScript as executable shell,
- DOM/SVG for text, geometry and data graphics,
- Canvas/WebGL only when complex compositing/particles/3D materially helps,
- generated/static images only as assets, not a screenshot substitute for the whole experience.

Design around a single mobile-first stage. Responsive adaptation may recompose the same semantic objects; it must not create contradictory meanings.

When implementing a controllable timeline, aim for a state model equivalent to:

```text
render(time, contentData, interactionState, viewport) -> visible scene
```

Seeking directly to a point should not produce a contradictory state compared with sequential playback.

## 7. Data / evidence contract

Keep factual content separate from visual choreography.

For each material claim preserve, where applicable:

- value,
- unit,
- baseline/comparator,
- date/time window,
- source/provenance,
- confidence/uncertainty,
- observed fact vs interpretation vs scenario/assumption.

Numeric labels and their visual encodings must derive from the same value. Never make bar length, area, position, count, speed, or causal arrows imply more than the source supports.

## 8. Domain-native surface law

Lead with the object that carries the domain meaning.

Examples:

- market/portfolio/probability → price, threshold, distribution, exposure, scenario, flow;
- news/inbox → ranked changes, source clusters, action queue, chronology;
- sports → score/points/table/remaining fixtures/position relation;
- operations → topology, state transition, bottleneck, dependency, failure boundary;
- scientific/engineering → physical object, variable relation, uncertainty, measurement geometry.

Text explains the object; it should not replace the object when the object can carry the claim.

## 9. Art direction

Each Vista gets a subject-appropriate visual world. Avoid one universal Campsite skin.

Control through design tokens:

- typography,
- spacing,
- hierarchy,
- color roles,
- line/shape language,
- depth/light,
- easing/rhythm,
- interaction feedback.

Aesthetics may be expressive. Data semantics remain strict.

The 2026 Chizumulu-quality work is a **quality calibration**, not a layout template.

## 10. Interaction

Default path: understandable without touching.

Optional interaction: deeper understanding when touched.

Suitable interactions include:

- select a comparison target,
- toggle an assumption/scenario,
- scrub time,
- manipulate a meaningful object,
- reveal evidence/source/context,
- pause on an object and inspect it.

Rules:

- user input updates one coherent state model;
- all dependent graphics/numbers/copy update together;
- manipulating while autoplay runs should pause or clearly transfer temporal control;
- provide a return/resume/reset path;
- do not make host publication/share/auth mutations from an untrusted artifact frame;
- keyboard/touch and reduced-motion paths should be supported where applicable.

## 11. Source / sharing safety

A Vista may contain only the audience context permitted for that artifact.

A future Trail publication must not inherit raw private audience memory merely because the private Vista used it during composition. Public/shared derivatives require an explicit approved artifact revision or host-side sanitization/review contract.

This skill does not grant publication authority.

## 12. Legacy wire compatibility

When a host still requires the existing Campsite BriefEnvelope/motion_brief shape, emit it without pretending those field names are current product nouns.

Compatibility shape:

```json
{
  "id": "string",
  "camp_id": "string",
  "origin": "cronlet | trail | session",
  "brief_type": "verdict | metric | ranked | report | quiet | plain",
  "attention_state": "attention | calm | quiet | failed",
  "artifact_format": "motion_brief",
  "confidence_level": "sufficient | limited | error",
  "title": "string",
  "scheduled_at": "ISO-8601",
  "scenes": [],
  "sources": [],
  "actions": [],
  "fallback_text": "required"
}
```

Important:

- This is a **transport compatibility contract**, not the canonical product domain model.
- Do not rename `camp_id`, `origin`, or `motion_brief` unless the owning schema changes.
- `fallback_text` remains mandatory when required by the host schema.
- One independent producer result should retain one independent canonical Vista identity.

## 13. Output modes

### Campsite adapter JSON-only mode

If the active adapter explicitly requires the existing JSON envelope, return exactly the required JSON object and no HTML/Markdown commentary.

### Default authoring mode

Produce:

1. **Vista HTML** — complete single-file HTML/SVG/JS unless assets/dependencies are explicitly allowed.
2. **Compatibility JSON** — when a host schema requires it.
3. **Self-check** — concise evidence, not marketing language.

Suggested self-check:

```text
Understanding objective: ...
Claim/evidence fidelity: ...
Domain object/art direction: ...
Interaction/state path: ...
Viewport/reduced-motion: ...
Host/runtime claims not proven here: ...
```

## 14. Artifact-level verification

Before calling a generated Vista complete, verify applicable rows:

- target mobile viewport (at least the host's declared device size),
- no clipping/overlap/overflow at key states,
- initial/meaningful/final timeline states,
- play/pause/seek/restart if supported,
- interaction change + return/reset,
- data label/visual encoding agreement,
- source/uncertainty honesty,
- reduced-motion behavior,
- sandbox/no-credential assumptions,
- missing/invalid input behavior.

Do not claim host-product completion from artifact tests. Vista persistence, Campfire feed behavior, Trail publication, Camp/Tent state, Stream persistence, cross-user permissions, and backward compatibility require evidence in the owning Campsite runtime.

If required evidence is missing: **partial / not yet closed**.
