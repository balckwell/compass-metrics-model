from datetime import date
from unittest import TestCase
from unittest.mock import patch

from compass_metrics.contributor_metrics import contributor_detail_list


class MileageFilterTest(TestCase):
    @patch("compass_metrics.contributor_metrics.get_contributor_list")
    def test_accepts_runtime_string_for_mileage_filter(self, get_contributors):
        get_contributors.return_value = [{
            "contributor": "alice",
            "contribution": 1,
            "contribution_without_observe": 1,
            "ecological_type": "individual participant",
            "organization": None,
            "contribution_type_list": [],
            "is_bot": False,
            "repo_name": "example/repo",
        }]

        result = contributor_detail_list(
            None, "index", date(2026, 6, 1), ["example/repo"],
            from_date=date(2026, 1, 1),
            filter_mileage="".join(["c", "o", "r", "e"]),
        )

        self.assertEqual(result["core_count"], 1)
        self.assertEqual(len(result["contributor_detail_list"]), 1)
        self.assertEqual(result["contributor_detail_list"][0]["mileage_type"], "core")


if __name__ == "__main__":
    import unittest

    unittest.main()
