# Assets
CurrentAssets = float(input("What is your Current Assets?: "))
FixedAssets = float(input("How much fixed assets do you have?: "))
Debts = float(input("How much debt do you currently have?: "))
TotalAssets = (CurrentAssets + FixedAssets)
NetWorth = TotalAssets - Debts

print(f"Your total Assets are: {TotalAssets: .2f}")
print(f"Your total debts are: {Debts: .2f}")
print(f"Your total net worth is: {NetWorth: .2f}")


