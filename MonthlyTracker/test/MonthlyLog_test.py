import unittest
import datetime
from MonthlyTracker.MonthlyLog import MonthlyLog
from MonthlyTracker.Entry import Entry


class MyTestCase(unittest.TestCase):

    def test_add_entry(self):
        test_month = MonthlyLog("September", "2020")
        test_entry = Entry("test", 2.34, "none", datetime.date(2020, 9, 3))

        test_month.add_entry(test_entry)

        expected = 1
        actual = test_month.get_entries_size()

        self.assertEqual(expected, actual)

    def test_remove_entry(self):
        test_month = MonthlyLog("September", "2020")
        test_entry = Entry("test", 2.34, "none", datetime.date(2020, 9, 3))

        test_month.add_entry(test_entry)
        test_month.remove_entry(0)

        expected = 0
        actual = test_month.get_entries_size()

        self.assertEqual(expected, actual)

    def test_print_entries(self):
        test_month = MonthlyLog("December", "2022")
        test_entry = Entry("test", 7.88, "none", datetime.date(2022, 12, 3))
        test_entry2 = Entry("test", 3.12, "none", datetime.date(2022, 12, 13))

        test_month.add_entry(test_entry)
        test_month.add_entry(test_entry2)

        expected = 'test 7.88 none 2022-12-03\ntest 3.12 none 2022-12-13\n'
        actual = test_month.print_entries()

        self.assertEqual(expected, actual)

    def test_calculate_sum(self):
        test_month = MonthlyLog("December", "2022")
        test_entry = Entry("test", 7.88, "none", datetime.date(2022, 12, 3))
        test_entry2 = Entry("test", 3.12, "none", datetime.date(2022, 12, 13))

        test_month.add_entry(test_entry)
        test_month.add_entry(test_entry2)

        expected = test_entry.value + test_entry2.value
        actual = test_month.calculate_sum()

        self.assertEqual(expected, actual)

    def test_overspending(self):
        test_month = MonthlyLog("December", "2022")
        test_entry = Entry("test", 200, "none", datetime.date(2022, 12, 3))

        test_month.set_spending_limit(199.99)
        test_month.add_entry(test_entry)

        expected = True
        actual = test_month.is_overspending()

        self.assertEqual(expected, actual)
