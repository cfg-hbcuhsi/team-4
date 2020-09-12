
class MonthlyLog:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.monthly_spending_limit = 500
        self.monthly_sum = 0
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)

    def get_entries_size(self):
        return len(self.entries)

    def print_entries(self):
        msg = ''
        for entry in self.entries:
            msg += entry.print_entry() + "\n"

        return msg
