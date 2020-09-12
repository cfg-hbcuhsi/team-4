from MonthlyTracker.Entry import Entry
from MonthlyTracker.MonthlyLog import MonthlyLog
import datetime


class Application:
    def __init__(self):
        self.current_day = '01'
        self.current_month = '01'
        self.current_year = '2000'
        self.get_current_date()  # 1/1/2000 is default date which the app immediately updates

        self.calender = []
        self.curr_calender_index = int(self.current_month)
        # Point to the current month by default.
        # This pointer is for manipulating data


    def get_current_date(self):
        today = str(datetime.date.today())
        current_date = datetime.datetime.strptime(today, "%Y-%m-%d")

        self.current_day = str(current_date.day)
        self.current_month = str(current_date.month)
        self.current_year = str(current_date.year)

    def generate_calender(self):
        self.get_current_date()
        # generate a month obj for every month this year
        months = range(1, 13)
        for month in months:
            self.calender.append(MonthlyLog(month, self.current_year))

    def create_append_entry(self, name, value, category, date):
        new_entry = Entry(name, value, category, date)
        self.curr_calender_index = int(new_entry.get_month())

        self.calender[self.curr_calender_index-1].add_entry(new_entry)

    def display_month_sum(self, index):
        self.curr_calender_index = index
        total = self.calender[self.curr_calender_index].calculate_sum()
        msg = ''
        msg += 'The month of ' + str(self.curr_calender_index+1) + ' has the spending sum of: ' + str(total)
        return msg

    def display_all_entries(self):
        msg = ''
        for month in self.calender:
            msg += month.print_entries()
        return msg

    def take_entry(self):
        print('Create a new entry: \n')
        name = input('Please enter the name for the purchase: ')
        value = input('How much did it cost?: ')
        category = input('What kind of purchase was it? ')
        bought_today = input('Was it purchased today? Y/N ')

        if bought_today in ['N', 'n']:
            day = input("Enter the day: ")
            month = input("Enter the month: ")
            year = input("Enter the year: ")
            date = year + "-" + month + '-' + day

        else:
            date = datetime.date.today()  # automatically use today's date if random input was used

        self.create_append_entry(name, value, category, date)
        print("Entry added!")


def main():
    Application().__init__()
    Application().generate_calender()
    Application().take_entry()


if __name__ == '__main__':
    main()



