from unittest.mock import patch, MagicMock

from django.test import TestCase
from pylint.pylint_badge import get_rating_and_colour
# Create your tests here.

class PylintBadgeServer(TestCase):
    maxDiff = None
    """
    Test rating_and_colour
    """
    @patch('pylint.pylint_badge.BADGE_TEMPLATE', '{1} {0:.2f}')
    def test_colour_report(self):
        report = "Your code has been rated at 6/10"
        colour_report = get_rating_and_colour(report)
        self.assertEqual(colour_report, 'b94947 6.00')

