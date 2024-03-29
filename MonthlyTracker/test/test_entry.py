import unittest
from MonthlyTracker.Entry import Entry
import datetime


class MyTestCase(unittest.TestCase):

    def test_get_name(self):
        test_entry = Entry("test", 2.34, "none", datetime.date(2021, 12, 3))

        expected = "test"
        actual = test_entry.name

        self.assertEqual(expected, actual)

    def test_get_value(self):
        test_entry = Entry("test", 5.90, "none", datetime.date(2021, 12, 3))

        expected = 5.9
        actual = test_entry.value

        self.assertEqual(expected, actual)

    def test_get_category(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2021, 12, 3))

        expected = "food"
        actual = test_entry.category

        self.assertEqual(expected, actual)

    def test_get_date(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2021, 12, 3))

        expected = datetime.date(2021, 12, 3)
        actual = test_entry.date

        self.assertEqual(expected, actual)

    def test_print_entry(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2021, 12, 3))

        expected = "test 5.9 food 2021-12-03"
        actual = test_entry.print_entry()

        self.assertEqual(expected, actual)

    def test_get_day(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2020, 12, 9))

        expected = '09'
        actual = test_entry.get_day()

        self.assertEqual(expected, actual)

    def test_get_month(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2020, 12, 9))

        expected = '12'
        actual = test_entry.get_month()

        self.assertEqual(expected, actual)

    def test_get_year(self):
        test_entry = Entry("test", 5.90, "food", datetime.date(2020, 12, 9))

        expected = '2020'
        actual = test_entry.get_year()

        self.assertEqual(expected, actual)
