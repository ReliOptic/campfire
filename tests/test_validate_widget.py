from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from tools.validate_widget import ValidationError, validate_widget

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "daily-macro-grammar-pass.json"


class DailyMacroDeliveryGrammarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.widget = json.loads(FIXTURE.read_text(encoding="utf-8"))

    def test_fixture_outer_widget_passes(self) -> None:
        validate_widget(self.widget)

    def test_rejects_bare_payload_without_outer_widget(self) -> None:
        with self.assertRaisesRegex(ValidationError, "outer widget"):
            validate_widget(self.widget["payload"])

    def test_rejects_copy_before_first_domain_object(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["scenes"][0]["say"] = "BTC와 QQQ는 상승했습니다."
        with self.assertRaisesRegex(ValidationError, "say/sub"):
            validate_widget(widget)

    def test_allows_grounding_kicker_before_first_domain_object(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["scenes"][0]["w"] = "오늘의 네 줄"
        validate_widget(widget)

    def test_rejects_missing_first_scene_domain_object(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["scenes"][0].pop("rows")
        with self.assertRaisesRegex(ValidationError, "rows"):
            validate_widget(widget)

    def test_rejects_num_only_first_scene_for_daily_macro(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["scenes"][0].pop("rows")
        widget["payload"]["scenes"][0]["num"] = {"v": "+2.1%"}
        with self.assertRaisesRegex(ValidationError, "rows"):
            validate_widget(widget)

    def test_rejects_unavailable_row_with_fabricated_direction(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["scenes"][0]["rows"][0] = {
            "k": "BTC/USD",
            "v": "확인 불가",
            "dir": "dn",
        }
        with self.assertRaisesRegex(ValidationError, "unavailable"):
            validate_widget(widget)

    def test_empty_actions_pass_when_summary_states_no_action(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["actions"] = []
        validate_widget(widget)

    def test_rejects_empty_actions_without_no_action_summary(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["actions"] = []
        widget["payload"]["scenes"][-1]["say"] = "요약입니다."
        widget["payload"]["scenes"][-1]["sub"] = "오늘 흐름만 정리합니다."
        with self.assertRaisesRegex(ValidationError, "empty actions"):
            validate_widget(widget)

    def test_word_action_alone_does_not_count_as_honest_no_action(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["actions"] = []
        widget["payload"]["scenes"][-1]["say"] = "행동 판단입니다."
        widget["payload"]["scenes"][-1]["sub"] = "요약입니다."
        with self.assertRaisesRegex(ValidationError, "empty actions"):
            validate_widget(widget)

    def test_rejects_forbidden_platform_action(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["actions"] = [
            {"label": "Open in Tent", "consequence": "Tent 화면을 엽니다."}
        ]
        with self.assertRaisesRegex(ValidationError, "forbidden"):
            validate_widget(widget)

    def test_rejects_equivalent_tent_storage_action(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["actions"] = [
            {"label": "Tent에 저장하기", "consequence": "Tent 화면에 보관합니다."}
        ]
        with self.assertRaisesRegex(ValidationError, "forbidden"):
            validate_widget(widget)

    def test_rejects_missing_source_why_limitation(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["sources"][0].pop("why")
        with self.assertRaisesRegex(ValidationError, "why"):
            validate_widget(widget)

    def test_rejects_stable_source_id_without_why_limitation(self) -> None:
        widget = copy.deepcopy(self.widget)
        widget["payload"]["sources"][0].pop("why")
        widget["payload"]["sources"][0]["stable_id"] = "hermes-yahoo-finance-2026-08-04"
        with self.assertRaisesRegex(ValidationError, "why"):
            validate_widget(widget)


if __name__ == "__main__":
    unittest.main()
