# Hermes 장착

| 항목 | 값 |
|---|---|
| SYSTEM | `SKILL.md` 본문 (frontmatter 제외) — 스킬 파일로 등록 |
| USER | pack YAML + run snapshot YAML + Deliver 지시 (README 조립 템플릿) |
| Tools | **off** — 스킬은 live fetch를 하지 않는다. 숫자는 snapshot이 전부다 |
| 출력 | 기본 저작은 PART 1 HTML · PART 2 JSON · PART 3 self-check 6줄; Campsite adapter는 아래 JSON-only override |

## Production cron 연동

- pack ≈ 잡 계약의 `output` 의도 (도메인 클래스·슬롯 카탈로그)
- snapshot ≈ 에이전트가 이번 실행에서 구조화한 결과
- 코어 스킬(SYSTEM)은 모든 잡이 공유 — 잡마다 SYSTEM을 복제하지 않는다

장기적으로 잡 계약의 output 블록에 `domain_class` / `pack_id`를 넣고,
런타임이 pack 레지스트리에서 골라 같은 코어 스킬을 호출하는 구조를 권장한다.


## Campsite adapter compatibility gate

Hermes cron prompts that target Campsite must feed the Campfire skill a structured
snapshot and emit exactly one outer widget JSON object:
`{"archetype":"motion_brief","archetype_version":"...","fallback_text":"...","payload":{...}}`.
Do not wrap it in PART 1 HTML or PART 3 commentary: the Campsite adapter's
`_detect_widget` path consumes a single JSON object with `archetype` and
`fallback_text`, not an HTML+JSON transcript. Do not send raw prose and expect
Campsite to infer a Campfire: the adapter forwards structured widget JSON and
promotes runtime identity, but it does not summarize, rank, or repair delivery
copy.

Before deploying a daily macro cron prompt, validate a representative widget:

```bash
python3 tools/validate_widget.py fixtures/daily-macro-grammar-pass.json
python3 -m unittest discover -s tests -v
```

The daily macro pack is rows-first. Scene 1 carries market rows with no
`say`/`sub` prose ahead of the object; a short `w` grounding kicker is allowed.
Current Campsite source wire does not
carry URL/stable-id identity here, so daily macro sources must include an
explicit `why` limitation. Actions may be empty only when the summary states an
honest no-action; any action that is present must be a real decision branch,
never host navigation such as `Open in Tent`.
