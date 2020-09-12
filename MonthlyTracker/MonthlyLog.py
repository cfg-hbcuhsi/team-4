class MonthLog:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.monthly_spending_limit = 500
        self.monthly_sum = 0
        self.entries = []
