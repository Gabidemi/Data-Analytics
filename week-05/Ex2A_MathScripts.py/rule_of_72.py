# Rule of 72
# Some pitfalls using input here would be not enough directions given on what to type
# This would then result in errors

CurrentSavings = float(input("What is your current savings?: "))
InterestRate = float(input("How much interest rate are you looking at?: "))
Years = 72//InterestRate
SavingsTimesTwo = CurrentSavings * 2

print(f"Your current savings is: {CurrentSavings: .2f}")
print(f"At a {InterestRate: .2f}% interest rate, " + 
    f"your savings account will be worth ${SavingsTimesTwo: .2f} in {Years} years"
)