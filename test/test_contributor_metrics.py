from datetime import date
from unittest import TestCase
from unittest.mock import patch

from compass_metrics.contributor_metrics import pr_review_contributor_count


class PRReviewContributorCountTest(TestCase):
    @patch("compass_metrics.contributor_metrics.get_contributor_count")
    def test_keeps_bot_and_non_bot_counts(self, get_count):
        get_count.side_effect = [10, 1, 9]

        result = pr_review_contributor_count(
            client=None,
            contributors_index="contributors",
            date=date(2026, 1, 1),
            repo_list=["example/repo"],
        )

        self.assertEqual(result, {
            "pr_review_contributor_count": 10,
            "pr_review_contributor_count_bot": 1,
            "pr_review_contributor_count_without_bot": 9,
        })
        self.assertEqual(get_count.call_count, 3)


if __name__ == "__main__":
    import unittest

    unittest.main()
