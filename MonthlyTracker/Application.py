from MonthlyTracker.Entry import Entry
import datetime


entry1 = Entry("test", 2.34, "none", datetime.date(2021, 12, 3))

print(entry1.date)
