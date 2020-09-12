import pandas as pd

#default age of user is 15
currentage = 15
#starting sum is an initial lump sum to invest, default is 0
startingsum = 0

# $20 is the default monthly investment
monthlyinvestmentdefault = 20
monthlyinvestment25 = monthlyinvestmentdefault
monthlyinvestment35 = monthlyinvestment25
monthlyinvestment50 = monthlyinvestment35

#monthstotrack is the total number of months from current age to 65
monthstotrack = int((65-currentage)*12)

#This is an array that tracks the total number of months investments will be made starting from 0
month = []
for i in range(monthstotrack):
    month.append(i)
    #print("month #", month[i])


#This array tracks the age of the user over time
atage = []
for i in range(monthstotrack):
    if month[i] % 12 == 0:
        atage.append(currentage + month[i]/12)
    else:
        atage.append("    ")

amountinvested = []
for i in range(monthstotrack):
    if i == 0:
        amountinvested.append(startingsum + monthlyinvestmentdefault)
    else:
        amountinvested.append(amountinvested[i-1] + monthlyinvestmentdefault)

valueofinvestment = []
for i in range(monthstotrack):
    if i == 0:
        valueofinvestment.append(amountinvested[i])
    else:
        valueofinvestment.append(valueofinvestment[i-1] + monthlyinvestmentdefault + (valueofinvestment[i-1] * 0.06 / 12))

for i in range(monthstotrack):
    print(month[i], atage[i], amountinvested[i], "  ", valueofinvestment[i])

# create dataframe
df_marks = pd.DataFrame({'age': atage,
     'amount invested': amountinvested,
     'value of investment': valueofinvestment})

# render dataframe as html
html = df_marks.to_html()
print(html)

