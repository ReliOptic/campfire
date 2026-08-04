#!/usr/bin/env python3
"""Validate producer-side Campfire widget delivery grammar.

This is intentionally small and stdlib-only. It checks the portable producer
contract for the actual Hermes -> Campsite adapter input: one outer widget
object with archetype, fallback_text, and payload. It does not replace the
Campsite envelope schema.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

FORBIDDEN_ACTION_LABELS = {"open in tent", "tent에 저장"}
MISSING_ROW_VALUES = {"", "-", "—", "n/a", "na", "null", "none", "unknown", "확인 불가"}
NO_ACTION_SIGNALS = (
    "새 행동은 만들지",
    "행동 없음",
    "행동할 필요",
    "관찰 결론",
    "관찰만",
    "no action",
)


class ValidationError(ValueError):
    pass


def _load(path: str | Path) -> dict[str, Any]:
    with Path(path).open(encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValidationError("widget must be a JSON object")
    return data


def unwrap_widget(data: dict[str, Any]) -> dict[str, Any]:
    if data.get("archetype") != "motion_brief":
        raise ValidationError("outer widget archetype must be motion_brief")
    if not data.get("archetype_version"):
        raise ValidationError("outer widget archetype_version is required")
    if not data.get("fallback_text"):
        raise ValidationError("outer widget fallback_text is required")
    payload = data.get("payload")
    if not isinstance(payload, dict):
        raise ValidationError("outer widget payload must be an object")
    return payload


def _has_explicit_source_limitation(source: dict[str, Any]) -> bool:
    why = source.get("why")
    return isinstance(why, str) and bool(why.strip())


def _is_missing_row_value(value: Any) -> bool:
    return str(value).strip().casefold() in MISSING_ROW_VALUES


def _is_forbidden_action_label(label: str) -> bool:
    normalized = " ".join(label.casefold().split())
    if normalized in FORBIDDEN_ACTION_LABELS:
        return True
    return "tent" in normalized or ("텐트" in normalized and any(token in normalized for token in ("열", "저장")))


def validate_widget(data: dict[str, Any]) -> None:
    payload = unwrap_widget(data)
    if payload.get("artifact_format") != "motion_brief":
        raise ValidationError("payload artifact_format must be motion_brief")
    scenes = payload.get("scenes")
    if not isinstance(scenes, list) or len(scenes) < 2:
        raise ValidationError("payload scenes must contain at least two scenes")
    first = scenes[0]
    if not isinstance(first, dict):
        raise ValidationError("first scene must be an object")
    if not first.get("rows"):
        raise ValidationError("first scene must lead with daily macro rows")
    if first.get("say") or first.get("sub"):
        raise ValidationError("first scene must not put say/sub copy before the domain object")
    rows = first.get("rows")
    if "rows" in first:
        if not isinstance(rows, list) or not rows:
            raise ValidationError("first scene rows must be a non-empty list")
        for i, row in enumerate(rows):
            if not isinstance(row, dict) or not row.get("k") or not row.get("v"):
                raise ValidationError(f"row {i} must include k and v")
            if _is_missing_row_value(row["v"]):
                raise ValidationError(f"row {i} must not encode an unavailable value")
    if not isinstance(scenes[-1], dict) or scenes[-1].get("summary") is not True:
        raise ValidationError("last scene must be marked summary:true")
    summary_text = " ".join(str(scenes[-1].get(key, "")) for key in ("say", "sub"))

    actions = payload.get("actions")
    if not isinstance(actions, list):
        raise ValidationError("payload actions must be a list")
    if not actions and not any(token in summary_text.lower() for token in NO_ACTION_SIGNALS):
        raise ValidationError("empty actions require an explicit no-action summary")
    recommended = 0
    for action in actions:
        if not isinstance(action, dict):
            raise ValidationError("each action must be an object")
        label = str(action.get("label", "")).strip()
        if _is_forbidden_action_label(label):
            raise ValidationError(f"forbidden platform action label: {label}")
        consequence = str(action.get("consequence", "")).strip()
        if len(consequence) < 8:
            raise ValidationError("action consequence must describe the outcome")
        if action.get("recommended") is True:
            recommended += 1
            if action.get("primary") is not True:
                raise ValidationError("recommended action must mirror primary:true")
    if recommended > 1:
        raise ValidationError("only one recommended action is allowed")

    sources = payload.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ValidationError("at least one source is required")
    if not all(isinstance(src, dict) and _has_explicit_source_limitation(src) for src in sources):
        raise ValidationError("each source needs an explicit why limitation")


def validate_path(path: str | Path) -> None:
    validate_widget(_load(path))


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_widget.py <widget.json>", file=sys.stderr)
        return 2
    try:
        validate_path(argv[1])
    except (OSError, json.JSONDecodeError, ValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print(f"OK: {argv[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
