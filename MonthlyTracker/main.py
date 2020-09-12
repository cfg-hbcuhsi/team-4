# This is a sample Python script.
import datetime
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    day = 20
    month = 2
    year = 2012

    testDate = datetime.date(year, month, day)
    testDate2 = datetime.date.today()

    print(testDate)
    print(testDate2)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
