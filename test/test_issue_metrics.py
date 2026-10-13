from datetime import date
from unittest import TestCase
from unittest.mock import patch

from compass_metrics.issue_metrics import time_to_close


class TimeToCloseTest(TestCase):
    @patch("compass_metrics.issue_metrics.get_all_index_data")
    def test_returns_empty_metrics_when_items_have_no_state(self, get_items):
        get_items.return_value = [
            {"_source": {"created_at": "2026-01-01T00:00:00", "uuid": "one"}},
            {"_source": {"created_at": "2026-01-02T00:00:00", "uuid": "two"}},
        ]

        result = time_to_close(
            client=None,
            issue_index="issues",
            date=date(2026, 3, 1),
            repos_list=["example/repo"],
        )

        self.assertEqual(result, {
            "time_to_close_avg": None,
            "time_to_close_mid": None,
        })


if __name__ == "__main__":
    import unittest

    unittest.main()
