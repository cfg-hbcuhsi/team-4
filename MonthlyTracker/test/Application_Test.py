import unittest
import datetime
from MonthlyTracker.Application import Application
from MonthlyTracker.MonthlyLog import MonthlyLog
from MonthlyTracker.Entry import Entry


class MyTestCase(unittest.TestCase):
    def test_get_curr_date(self):
        test_application = Application()

        test_application.get_current_date()

        expected_day = '12'
        actual_day = test_application.current_day

        expected_month = '9'
        actual_month = test_application.current_month

        expected_year = '2020'
        actual_year = test_application.current_year

        self.assertEqual(expected_day, actual_day)
        self.assertEqual(expected_month, actual_month)
        self.assertEqual(expected_year, actual_year)

    def test_generate_calender(self):
        test_application = Application()

        test_application.generate_calender()

        expected = 12
        actual = len(test_application.calender)

        self.assertEqual(expected, actual)

    def test_generate_entry(self):
        test_application = Application()
        test_application.generate_calender()

        test_application.create_append_entry('entry1', 100.00, 'clothes', datetime.date(2020, 2, 3))

        expected = 1
        actual = test_application.calender[1].get_entries_size()

        self.assertEqual(expected, actual)

    def test_display_sum(self):
        test_application = Application()
        test_application.generate_calender()

        test_application.create_append_entry('entry1', 100.00, 'clothes', datetime.date(2020, 2, 3))
        test_application.create_append_entry('entry2', 100.00, 'clothes', datetime.date(2020, 2, 3))

        expected = 'The month of 2 has the spending sum of: 200.0'
        actual = test_application.display_month_sum(1)
        self.assertEqual(expected, actual)

    def test_print_all_entries(self):
        test_application = Application()
        test_application.generate_calender()

        test_application.create_append_entry('entry1', 100.00, 'clothes', datetime.date(2020, 2, 3))
        test_application.create_append_entry('entry2', 100.00, 'clothes', datetime.date(2020, 12, 8))
        test_application.create_append_entry('entry3', 100.00, 'clothes', datetime.date(2020, 6, 10))

        expected = 'entry1 100.0 clothes 2020-02-03\nentry3 100.0 clothes 2020-06-10\nentry2 100.0 clothes 2020-12-08\n'
        actual = test_application.display_all_entries()
        self.assertEqual(expected, actual)
