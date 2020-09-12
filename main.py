import pandas as pd
#creates an array of sequential numbers corresponding to months in the future
#def months(month, age, d, m, invested, value):
def everything(monthly_investment_at_age_15, monthly_investment_at_age_25,
               monthly_investment_at_age_35, monthly_investment_at_age_50):
    starting_sum = 0;
    current_age = 15
    retirement_age = 65
    months_to_track = int(
        (retirement_age - current_age) * 12 + 1)  # monthstotrack is the total number of months from current age to 65
    month = []  # the total number of months investments will be made starting from 0
    at_age = []  # the age of the user over time
    monthly_investment = []  # the amount investmented each month
    amount_invested = []  # running total amount invested
    value_of_investment = []  # array showing the net worth month-to-month up until retirement
    for i in range(months_to_track):
        month.append(i)
#creates an 'timeilne' array corresponding to the age of the user
#def at_what_age(age, d, m, invested, value):
    for i in range(months_to_track):
        if month[i] % 12 == 0:
            at_age.append(current_age + month[i] / 12)
        else:
            at_age.append("    ")
#monthly deposit
#def monthly(d, m):
#def monthly(d, m, invested, value):
    for i in range(months_to_track):
        if month[i] >= 0 and month[i] < 120:
            monthly_investment.append(monthly_investment_at_age_15)
        elif month[i] >= 120 and month[i] < 240:
            monthly_investment.append(monthly_investment_at_age_25)
        elif month[i] >= 240 and month[i] < 420:
            monthly_investment.append(monthly_investment_at_age_35)
        elif month[i] >= 420:
            monthly_investment.append(monthly_investment_at_age_50)
#total amount invested each month over time
#def invest(invested):
#def invest(invested, value):
    for i in range(months_to_track):
        if i == 0:
            amount_invested.append(starting_sum + monthly_investment[i])
        else:
            amount_invested.append(amount_invested[i - 1] + monthly_investment[i])
#total value of the investments over time
#def calculate_wealth(value):
    for i in range(months_to_track):
        if i == 0:
            value_of_investment.append(amount_invested[i])
        else:
            value_of_investment.append(
                value_of_investment[i - 1] + monthly_investment[i] + (value_of_investment[i - 1] * 0.06 / 12))
    thisdict = {
        "invested: running total": amount_invested,
        "total value of investments": value_of_investment,
    }
    print(thisdict)


#default age of user is 15
#starting_sum = 0 #can be changed to a variable
monthly_investment_at_age_15 = 20 #can be changed to a variable
monthly_investment_at_age_25 = 75 #can be changed to a variable
monthly_investment_at_age_35 = 125 #can be changed to a variable
monthly_investment_at_age_50 = 200 #can be changed to a variable

everything(monthly_investment_at_age_15, monthly_investment_at_age_25,
           monthly_investment_at_age_35, monthly_investment_at_age_50)

