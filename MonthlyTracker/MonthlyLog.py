
class MonthlyLog:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.monthly_spending_limit = 500.00
        self.monthly_sum = 0
        self.entries = []

    def add_entry(self, entry):
        self.entries.append(entry)
        self.calculate_sum()

    def remove_entry(self, index):
        if 0 <= index <= self.get_entries_size():  # Will only act if entry is valid
            self.entries.pop(index)
            self.calculate_sum()

    def get_entries_size(self):
        return len(self.entries)

    def print_entries(self):
        msg = ''
        for entry in self.entries:
            msg += entry.print_entry() + "\n"

        return msg

    def set_spending_limit(self, limit):
        self.monthly_spending_limit = limit

    def calculate_sum(self):
        total = 0
        for entry in self.entries:
            total += entry.value

        self.monthly_sum = total
        return total

    def is_overspending(self):
        if self.monthly_sum > self.monthly_spending_limit:
            return True
        else:
            return False
