# Tips

MealCost = float(input('What is the cost of your meal?: '))
TipAmount = 0.20
CustomerTip = 0.20 * MealCost
CustomerTax = 0.0825 * MealCost
TotalMealCost = MealCost + CustomerTip + CustomerTax

print(f"The tip for the meal is: {TipAmount: .2%} for a ${MealCost: .2f} order")
print(f"This amounts to (Including Taxes): ${TotalMealCost: .2f}")