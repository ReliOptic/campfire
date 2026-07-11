# ChatGPT 장착

| 항목 | 값 |
|---|---|
| SYSTEM | Custom instructions(또는 Custom GPT의 Instructions)에 `SKILL.md` 본문 (frontmatter 제외) |
| USER | pack YAML + run snapshot YAML + Deliver 지시 (README 조립 템플릿) |
| 출력 받기 | Canvas 또는 코드블록으로 HTML·JSON 저장 |

주의:

- 웹 브라우징을 꺼라 — 숫자는 snapshot이 전부이고, 스킬은 숫자 발명을 금지한다.
- Instructions 길이 제한에 걸리면 Custom GPT의 Knowledge에 `SKILL.md`를 올리고
  Instructions에는 "첨부된 SKILL.md를 SYSTEM 규칙으로 따르라"만 남겨도 된다.
