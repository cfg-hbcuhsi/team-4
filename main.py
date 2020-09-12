import pandas as pd

#creates an array of sequential numbers corresponding to months in the future
def months(month):
    for i in range(months_to_track):
        month.append(i)


#creates an 'timeilne' array corresponding to the age of the user
def at_what_age(age):
    for i in range(months_to_track):
        if month[i] % 12 == 0:
            age.append(current_age + month[i] / 12)
        else:
            age.append("    ")


#monthly deposit
def monthly(d, m):
    for i in range(months_to_track):
        if m[i] >= 0 and m[i] < 120:
            d.append(20)
        elif m[i] >= 120 and m[i] < 240:
            d.append(75)
        elif m[i] >= 240 and m[i] < 420:
            d.append(125)
        elif m[i] >= 420:
            d.append(200)


#total amount invested each month over time
def invest(invested):
    for i in range(months_to_track):
        if i == 0:
            invested.append(starting_sum + monthly_investment[i])
        else:
            invested.append(invested[i - 1] + monthly_investment[i])


#total value of the investments over time
def calculate_wealth(value):
    for i in range(months_to_track):
        if i == 0:
            value.append(amount_invested[i])
        else:
            value.append(
                value[i-1] + monthly_investment[i] + (value[i - 1] * 0.06 / 12))


#default age of user is 15
current_age = 15
#starting sum is an initial lump sum to invest, default is 0
starting_sum = 0

# $20 is the default monthly investment for a 15 year-old student
#monthly_investment = 20

#monthstotrack is the total number of months from current age to 65
months_to_track = int((65 - current_age) * 12 + 1)

#This is an array that tracks the total number of months investments will be made starting from 0
month = []
months(month)

#This array tracks the age of the user over time
at_age = []
at_what_age(at_age)

monthly_investment = []
monthly(monthly_investment, month)

amount_invested = []
invest(amount_invested)

value_of_investment = []
calculate_wealth(value_of_investment)

#prints values
#for i in range(months_to_track):
#    print(month[i], at_age[i], amount_invested[i], "  ", value_of_investment[i])

# create dataframe
df_marks = pd.DataFrame({
     'amount invested': amount_invested,
     'value of investment': value_of_investment})

# render dataframe as html
html = df_marks.to_html()
print(html)
