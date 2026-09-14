# Campfire skill — Vista composer compatibility package

> **2026-09-14 product canon:** 이 저장소와 스킬 호출명 `campfire`는 호환성을 위해 유지하지만, 이 스킬이 만드는 제품 객체의 이름은 **Vista**입니다.

Campsite의 현재 의미는 다음과 같습니다.

```text
Camp      = project/context
Tent      = conversation thread
Vista     = interactive visual artifact
Campfire  = personalized Vista feed
Trail     = verified publisher/channel
Stream    = realtime talk + show
```

따라서 이 Repo의 역할은 **원문/구조화 스냅샷을 고품질 Vista render bundle로 변환하는 제작 스킬**입니다.

```text
원문 / 구조화 스냅샷
        ↓
[legacy invocation: campfire skill]
        ↓
Vista render bundle
  ├─ playable HTML/SVG
  └─ legacy-compatible motion_brief / BriefEnvelope payload
```

`motion_brief`, `camp_id` 등 기존 wire field는 Campsite schema가 실제 migration되기 전까지 호환성 계약으로 유지합니다. 제품 용어를 맞춘다는 이유로 wire를 임의 변경하지 않습니다.

## 이 Repo가 소유하는 것

- Vista의 정보 서사와 장면 설계
- 광고급 art direction + 데이터 저널리즘급 정확성
- HTML/SVG 기반 playable interaction
- domain pack / run snapshot을 이용한 사실 보존
- 호스트에 전달할 compatibility payload
- artifact-level self-check와 fidelity evidence

## 이 Repo가 소유하지 않는 것

- **Campfire** 개인화 feed/ranking
- **Trail** publisher verification, publish/correct/withdraw/revoke
- **Camp / Tent** persistence
- **Stream** realtime session/persistence
- 사용자 auth/permission

이 기능들은 Campsite 제품 런타임에서 닫혀야 합니다. 이 스킬의 HTML 출력이 잘 재생된다는 이유만으로 그 동작이 구현됐다고 주장하지 않습니다.

## 제작 철학

목표는 “문장을 예쁘게 움직이는 것”이 아니라 **이해가 일어나는 장면**입니다.

- 사실·수치·단위·기준 시점·출처를 연출과 분리합니다.
- 같은 대상은 가능하면 동일한 시각 객체 정체성을 유지하며 변화합니다.
- 모션은 주의, 관계, 변화, 연속성을 설명해야 합니다.
- 사용자가 손대지 않아도 기본 경로로 이해되고, 조작하면 더 깊어져야 합니다.
- 주제마다 다른 아트 디렉션을 허용합니다. 범용 다크 카드 템플릿을 제품 정체성으로 만들지 않습니다.
- 개인화는 설명의 경로를 바꿀 수 있지만 사실의 결론을 바꾸지 않습니다.

과거 v3의 카드/타이밍/allowlist는 **compatibility heuristic**일 뿐 현재 제품의 창작 상한이 아닙니다. 특히 고정된 8–20초 길이, 제한된 모션 프로퍼티, 문장 fade/slide 중심 구성은 새 Vista의 필수 규칙이 아닙니다.

## 구조

| 층 | 역할 | 변경 주기 |
|---|---|---|
| **Core skill** ([SKILL.md](SKILL.md)) | Vista 제작 원칙 + compatibility output | 버전 관리 |
| **Domain pack** ([packs/](packs/)) | 도메인 슬롯·트리거·오브젝트 힌트 | 주제별 |
| **Run snapshot** ([snapshot/](snapshot/)) | 이번 실행의 사실/수치 | run별 |

팩은 시각 템플릿을 강제하지 않고, 숫자를 발명하지 않습니다.

## 실행 형식

기본 authoring 산출물은 다음을 지원합니다.

1. **playable HTML/SVG Vista render bundle**
2. **BriefEnvelope-compatible JSON** (legacy transport compatibility)
3. **self-check / closure receipt**

Campsite adapter가 JSON-only를 요구하면 해당 transport contract를 따릅니다. transport가 달라도 사실 정합성과 Vista 품질 기준은 동일합니다.

## Fidelity

이 스킬은 단독으로 호스트 플랫폼의 전체 완결성을 증명할 수 없습니다.

- HTML에서 구현·검증한 interaction/timeline은 artifact-level evidence입니다.
- Vista revision 저장, Campfire feed, Trail publishing, Stream persistence, permission은 Campsite runtime evidence가 필요합니다.
- “full cinema”, “production-ready”, “published” 같은 표현은 실제 증거 범위를 넘어 사용하지 않습니다.

완료 판정은 [`PRODUCT_CLOSURE_GUARDRAIL.md`](PRODUCT_CLOSURE_GUARDRAIL.md), 작업 원칙은 [`AGENTS.md`](AGENTS.md)를 따릅니다.

## 런타임별 장착

| 런타임 | 가이드 |
|---|---|
| Hermes | [adapters/hermes.md](adapters/hermes.md) |
| Claude / Claude Code | [adapters/claude.md](adapters/claude.md) |
| ChatGPT | [adapters/chatgpt.md](adapters/chatgpt.md) |

런타임은 제작 공급자입니다. 제품 데이터와 발행 권한은 Campsite가 소유합니다.

## Migration note

이 공개 Repo의 이름을 즉시 `vista`로 바꾸지는 않습니다. 기존 설치/링크/스킬 호출 호환성을 깨뜨릴 수 있기 때문입니다.

```text
package/repo invocation: campfire   (legacy compatibility)
product artifact noun: Vista        (canonical)
product feed noun: Campfire         (canonical)
```

이 구분이 없어지는 실제 rename은 downstream 사용처와 wire/schema migration이 증명된 별도 작업으로 다룹니다.

## License

[MIT](LICENSE)
