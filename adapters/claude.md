# Claude 장착

## Claude Code (스킬)

```bash
# 개인 스킬로 설치
mkdir -p ~/.claude/skills/campfire
curl -fsSL https://raw.githubusercontent.com/ReliOptic/campfire/main/SKILL.md \
  -o ~/.claude/skills/campfire/SKILL.md
```

또는 프로젝트 스킬: 리포를 클론해 `.claude/skills/campfire/SKILL.md`로 복사.
이후 대화에서 pack + snapshot을 붙이고 "Campfire로 넘겨"라고 하면 된다.

## Claude 앱 (claude.ai)

| 항목 | 값 |
|---|---|
| Project instructions | `SKILL.md` 본문 (frontmatter 제외) |
| 메시지 | pack YAML + run snapshot YAML + Deliver 지시 (README 조립 템플릿) |
| 출력 받기 | Artifacts로 HTML 재생 + JSON 저장 |
