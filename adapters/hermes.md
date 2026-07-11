# Hermes 장착

| 항목 | 값 |
|---|---|
| SYSTEM | `SKILL.md` 본문 (frontmatter 제외) — 스킬 파일로 등록 |
| USER | pack YAML + run snapshot YAML + Deliver 지시 (README 조립 템플릿) |
| Tools | **off** — 스킬은 live fetch를 하지 않는다. 숫자는 snapshot이 전부다 |
| 출력 | PART 1 HTML · PART 2 JSON · PART 3 self-check 6줄 |

## Production cron 연동

- pack ≈ 잡 계약의 `output` 의도 (도메인 클래스·슬롯 카탈로그)
- snapshot ≈ 에이전트가 이번 실행에서 구조화한 결과
- 코어 스킬(SYSTEM)은 모든 잡이 공유 — 잡마다 SYSTEM을 복제하지 않는다

장기적으로 잡 계약의 output 블록에 `domain_class` / `pack_id`를 넣고,
런타임이 pack 레지스트리에서 골라 같은 코어 스킬을 호출하는 구조를 권장한다.
