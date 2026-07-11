# Campfire — 에이전트가 부르는 audience-of-one 브리프 변환 스킬

> 에이전트 유저가 Campfire 스킬을 켜면, 어떤 도메인이든 같은 전달 규칙으로 결과를 받는다.

크론 잡이나 에이전트 루틴의 산출물은 보통 긴 텍스트 로그로 도착합니다.
Campfire는 그 자리에 끼우는 **표준 변환기**입니다:

```
원문 / 구조화 스냅샷  →  [Campfire skill]  →  motion_brief JSON + 재생 가능한 HTML
```

결과물은 "결과 예쁘게 쓰기"가 아니라, 한 명의 독자를 위한 저널리즘입니다 —
그 사람의 규칙·포지션·행동에 비추어 **무엇·왜·그래서 뭐**를 한 호흡에 전달합니다.

## 구조 — 문법은 하나, 주제는 pack, 숫자는 snapshot

| 층 | 역할 | 바뀌는 주기 |
|---|---|---|
| **Core skill** ([SKILL.md](SKILL.md)) | 전달 품질 + 플레이어 문법 + wire 계약 | 불변 (동결본) |
| **Domain pack** ([packs/](packs/)) | 그 잡의 슬롯·트리거·오브젝트 힌트 | 주제마다 교체 |
| **Run snapshot** ([snapshot/](snapshot/)) | 이번 실행의 수치 | run마다 교체 |

도메인마다 SYSTEM을 복제하지 않습니다. 코어는 도메인 중립이고,
팩은 레이아웃을 고정하지 않으며(힌트만 제공), 숫자는 스냅샷이 전부입니다 —
**스킬은 숫자를 발명하지 않습니다.**

## 빠른 시작

1. **SYSTEM** = [SKILL.md](SKILL.md) 본문 (frontmatter 제외)
2. **USER** = 아래 템플릿

```text
# Domain pack
<packs/*.yaml 중 하나, 또는 packs/_schema.yaml로 직접 작성>

# Run snapshot
<snapshot/run-snapshot.yaml 형식으로 이번 실행 값 채움>

# Deliver
PART 1 HTML · PART 2 JSON · PART 3 self-check (six lines)
No web. No invention. Follow universal v3 core.
```

실행 예시는 [snapshot/examples/portfolio-risk.yaml](snapshot/examples/portfolio-risk.yaml)를 보세요.

## 도메인 클래스 8종

| Class | 예 | brief_type | attention 기본 | Hero object 기본 |
|---|---|---|---|---|
| **threshold** | 포트폴리오 리스크 한도 감시 | verdict | 위반 시 attention | `num`+`band` (your line) |
| **pulse** | 일일 매크로 지표 | metric | calm | `rows` 보드 (4–6 keys) |
| **ranked** | 뉴스·예측시장 다이제스트 | ranked | 상위 델타에 따라 | `items` 순위 + delta |
| **flow** | 수급/자금 흐름 보드 | metric | calm | `rows` 순매수 + 방향 |
| **digest** | 주간 종합 | report | calm | `items`/`steps` + 한 줄 |
| **ops_quiet** | 시스템 헬스 체크 | quiet/plain | quiet | quiet row (플레이어 서커스 금지) |
| **inbox** | 아침 메일 액션 큐 | ranked/verdict | 액션>0이면 attention | `items` 큐 + CTA 1개 |
| **regime** | 주간 레짐 판정 | report/verdict | calm | 레짐 선언 한 줄 + gauges |

각 클래스의 시드 팩이 [packs/](packs/)에 있습니다.

**L2 규칙 (보편):** `attention`이거나 pack이 `l2_required: true`면 하나의 시각 형태가
곧 주장이어야 합니다 (portfolio면 band, ranked면 1위 갭 바). quiet에 L2를 시도하는 것
자체가 실패(과잉)입니다.

## 런타임별 장착

| 런타임 | 가이드 |
|---|---|
| Hermes | [adapters/hermes.md](adapters/hermes.md) — 스킬 파일 등록, tools off |
| Claude / Claude Code | [adapters/claude.md](adapters/claude.md) — 스킬 설치 또는 Project instructions |
| ChatGPT | [adapters/chatgpt.md](adapters/chatgpt.md) — Custom instructions / Custom GPT |

## 출력 계약

- **PART 1** — 완결된 단일 HTML 파일 (플레이어: TAP NEXT · hold pause · reduced-motion)
- **PART 2** — BriefEnvelope 호환 motion_brief JSON. `fallback_text` 필수 —
  **위젯 때문에 메시지가 유실되는 일은 절대 없다.** 마지막 씬은 `summary: true`
- **PART 3** — self-check 6줄 (Decision / One-liner / Domain fit / Load / L2 / gates)

여러 런타임에서 같은 품질이 나오는지는 [scoring.md](scoring.md)로 검증합니다.

## 출처

[Campsite](https://github.com/ReliOptic) 제품의 Campfire 전달 문법(2026-07-11 동결)에서
파생된 단독 스킬입니다. 출력 JSON은 Campsite gateway ingest로 그대로 꽂을 수 있는
형태이지만, 이 스킬 자체는 Campsite 없이도 독립적으로 동작합니다.

## License

[MIT](LICENSE)
