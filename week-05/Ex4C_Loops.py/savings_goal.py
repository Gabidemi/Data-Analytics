balance = 20
savings_goal = 100
weekly_savings = 20
treat_cost = 10
treat_bought = 0

while balance < savings_goal:
    balance = balance + weekly_savings
    if balance >= savings_goal * 0.75 and treat_bought == 0:
        balance = balance - treat_cost
        treat_bought = 1
        print("So close! After treating myself, my balance is up to " + str(balance) + ".")
    elif balance > savings_goal * 0.50:
        print("Almost there! This week my balance is up to " + str(balance) + ".")
    else:
        print("This week my balance increased to " + str(balance) + ".")
print("Goal met! My current balance is " + str(balance) + ".")