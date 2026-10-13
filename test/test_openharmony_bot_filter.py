from datetime import date
from unittest import TestCase
from unittest.mock import patch

from compass_metrics import contributor_metrics
from compass_metrics_v2 import contributor_metrics_v2


CONTRIBUTOR = {
    "contributor": "ci",
    "contribution": 1,
    "contribution_without_observe": 1,
    "ecological_type": "individual participant",
    "organization": None,
    "contribution_type_list": [],
    "is_bot": False,
    "repo_name": "example/repo",
}


class OpenHarmonyBotFilterTest(TestCase):
    def test_v1_keeps_unrelated_username_containing_bot_name(self):
        with patch.object(contributor_metrics, "get_contributor_list", return_value=[CONTRIBUTOR]):
            result = contributor_metrics.contributor_detail_list(
                None, "index", date(2026, 6, 1), ["example/repo"],
                from_date=date(2026, 1, 1),
            )
        self.assertEqual(result["core_count"], 1)
        self.assertEqual(result["contributor_detail_list"][0]["contributor"], "ci")

    def test_v2_keeps_unrelated_username_containing_bot_name(self):
        with patch.object(contributor_metrics_v2, "get_contributor_list", return_value=[CONTRIBUTOR]):
            result = contributor_metrics_v2.contributor_detail_list(
                None, "index", date(2026, 6, 1), ["example/repo"],
                from_date=date(2026, 1, 1),
            )
        self.assertEqual(result["core_count"], 1)
        self.assertEqual(result["contributor_detail_list"][0]["contributor"], "ci")


if __name__ == "__main__":
    import unittest

    unittest.main()
