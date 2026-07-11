---
name: campfire
description: 원문 또는 구조화 스냅샷을 audience-of-one Campfire 브리프(motion_brief JSON + 재생 가능한 HTML)로 변환한다. 도메인 무관 코어 — 주제는 pack, 숫자는 snapshot이 공급한다.
---

# Skill: Campfire composer — universal v3
# Freeze: 2026-07-11 · domain-agnostic core

## Job
**Lower cognitive load. Deliver the point sharp.**
한국어: 인지 부담을 덜어 주면서 내용은 선명하게.
끝나면 보는 이가 무엇·왜·그래서 뭐를 한 호흡으로 말한다.

NOT: slide decorator · dashboard reel · log/CoT printer · chrome demo ·
generic "market news for everyone".
ARE: audience-of-one delivery skill — journalism on *their* rules/positions/actions.

## Inputs you will receive
1) A **Domain pack** (class, through-line template, slots, CTA templates, L2 flag)
2) A **Run snapshot** (today's values only; no live fetch)

If pack and snapshot conflict on a number, **snapshot wins**.
If a slot is missing, drop it or mark confidence limited — never invent.

## Authority (higher wins)
1. Job (load ↓ + sharp ↑)
2. Journalism gates
3. This grammar
4. Wire field names (no silent renames)
5. Visual polish is downstream

## Family look
INVARIANT: w→say→sub→evidence→caption; tap=next; journalism; motion allowlist
(count/fill/opacity/gap/rise/scaleX); flip/source law; slim decision card;
slate hot for priority data; consequence=light (ink-invert), not orange heat.
VARIABLE: scene count 3–6; beat; viz within tokens; tone within voice.
Never freeze a topic-only layout. keep/freeze two-column is optional surgical only.

## Domain adaptation (Surface Law)
- Market / portfolio / probability → lead with numbers, prices, thresholds, gauges, splits
- News / inbox / conversation → lead with ranked items, queues, clusters, sources
- Explanation is secondary; evidence expands; **item count is never the whole artifact**
- Prefer objects from pack.preferred_objects that the snapshot actually fills
- Do not force portfolio band layout onto ranked news (or vice versa)

## Success
A) Load ↓: one through-line; one fact/comparison per scene; no "where to look?";
   no monologue; ≤1 recommended CTA (+ optional secondary)
B) Sharp ↑: conclusion · one evidence object · next action; cover test
L1 floor: mineral calm; no empty voids; zones respected

### L2 impact
If pack.l2_required is true OR (auto and attention_state=attention):
  Pass ≥4/6 of the L2 checklist (see scoring.md §L2); ONE form IS the claim.
If quiet/plain or l2_required false: do NOT force spectacle — L2 exempt.

## Journalism
- One decision/question for the whole brief (from pack.through_line_template + snapshot)
- No meta-count leads; no teaser without later delivery
- Organic arc; info gain; summary no new facts
- Comparisons need visuals
- No invented numbers
- confidence_level honest

## Type stack (no schema rename)
w=kicker (no §paths) · say=headline ≤2 lines · sub=standfirst (context OR so-what)
Evidence objects · optional chips. JSON: \n for line break; no raw <br> in envelope.

## Zones
orientation → statement → evidence → consequence (top flow, no fill-hole)

## Arc + beat
stake/lede → hero change → evidence/scan → optional risk → land/summary
Each scene: "beat": "lede"|"evidence"|"scan"|"land" when possible.

## Pacing
BASE: d=1.5+chars/21; summary×0.82; clamp 2.6–8.5
EDIT: beat may bias hold; avoid all scenes stuck at ceiling
Seg ∝ dur; total ~8–20s when possible; entrance order = hierarchy

## Player (HTML)
392px; TAP NEXT; body tap=next; hold≥400ms pause; seg seek;
Enter/→ next; Space pause; reduced-motion OK
Hot=#33404E; financial duotone only on market rows
CTA ink-invert; slim card (recommended tag, not dark-fill monopoly)

## Motion allowlist
ALLOWED: count fill opacity gap rise scaleX
BANNED decoration: bounce glitch 3D cinematic MP4-body rainbow

## N2 parody
Only if pack allows and: not data claim · ≤1s · collapse end · once · low chroma

## Flip / source
Front=edited brief; back/panel=immutable source (snapshot or original_source)
Chrome control only — never body-tap. Source panel OK as flip substitute.

## Decision slim
Equal visual weight; recommended=small tag; consequence≥8;
dismiss=defer

## Voice + copy gate
해요체 + dry wit ~70%; ≤1 metaphor/scene; roast systems not people;
CTA=outcome fork. Copy gate 6 checks (headline scene, standfirst why-now,
no §paths, action sentences, CTA branch, no abuse).

## Wire: motion_brief JSON
Emit a BriefEnvelope-compatible object:

```
{
  "id": string,
  "camp_id": string,                    // target inbox; "" if unknown
  "origin": "cronlet" | "trail" | "session",
  "brief_type": "verdict" | "metric" | "ranked" | "report" | "quiet" | "plain",
  "attention_state": "attention" | "calm" | "quiet" | "failed",
  "artifact_format": "motion_brief",    // "quiet_row" | "plain_text" for ops-quiet
  "confidence_level": "sufficient" | "limited" | "error",
  "title": string,
  "scheduled_at": ISO-8601 with offset,
  "scenes": [
    { "w"?, "say"?, "sub"?, "num"?, "band"?, "items"?, "gauges"?, "rows"?,
      "steps"?, "caution"?, "chips"?, "summary"?,
      "beat"?: "lede"|"evidence"|"scan"|"land" }
  ],
  "sources": [ { "title", "source_type": "gmail"|"web"|"calendar"|"repo"|"manual",
                 "fresh"?, "trust"?, "quote"?, "why"? } ],
  "actions": [
    { "label": string,
      "consequence": string,            // ≥8 chars — 일어날 일을 문장으로
      "recommended"?: boolean,
      "primary"?: boolean }             // recommended와 함께 primary:true도 설정 (shipping-schema 필드)
  ],
  "fallback_text": string,              // REQUIRED — 위젯 때문에 메시지가 유실되는 일은 없다
  "original_source"?: { "format": "text", "content": string }
}
```

Scene object shapes:

```
num    { v: number|string, dec?: 0-2, suf?: string, hot?: bool }
band   { max: 0-1, at: 0-1, lo: string, hi: string }      // your-line threshold bar
items  [ { n?: rank, t: title, d?: detail, delta?: string, dir?: "up"|"dn" } ]  max 5
rows   [ { k, v, s?: sub, dir?: "up"|"dn", badge?: "ok"|"wait", bar?: {v: 0-1} } ]  max 6
gauges [ { q: question, yes: 0-100, hot?: bool } ]  max 4
steps  [ string ]  max 5 · caution: string · chips: [string]  max 4
```

Rules:
- Scene must carry ≥1 of say/num/items/gauges/rows/steps. Scenes max 8.
- ≥2 scenes; **last scene summary: true**
- Every action has consequence; ONE recommended max — mirror it as `primary: true`
- `beat` / `recommended` / `original_source` are extensions: strict validators may
  **strip** them, so a player that wants beat must read the raw JSON, not the
  validated copy
- `original_source.content` if present = snapshot prose, not a new rewrite
- origin / brief_type / attention_state from pack + snapshot rules

## Process
1. Read pack → name through-line for THIS run
2. Map snapshot → slots; drop empty; pick objects per Surface Law
3. Choose attention_state (pack default + breach rules if pack defines)
4. Arc + beats; L2 only if required
5. Slim CTAs from templates filled by snapshot
6. HTML + JSON + self-check

## Output
PART 1: HTML (complete single file, inline CSS+JS; same scene data as JSON;
TAP NEXT, hold pause, seg seek, reading-time durations, keyboard + reduced-motion)
PART 2: JSON (BriefEnvelope + optional extensions; no commentary inside)
PART 3: six lines —
Decision: ...
One-liner (what/why/so-what): ...
Domain class + hero object: ...
Load removed: ...
L2: pass|exempt|fail — ...
Cover-test + copy-gate: ...
