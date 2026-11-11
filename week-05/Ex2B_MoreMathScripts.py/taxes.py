# Taxes

Salary = float(input("What is your current Salary? "))
Taxes = 0.23
TaxAmount = Taxes * Salary
Total = Salary - TaxAmount

print(f"You're owing ${TaxAmount: .2f} in taxes")
print(f"You're taking home ${Total: .2f} after your taxes")
