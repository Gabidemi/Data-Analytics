name1 = 'Ardita mrapshtija'
name2 = 'Moses Jura'
print(f"My two classmates are {name1} and {name2}!")


Item1 = 25.75
Item2 = 45.67
Item3 = 45.75
Item4 = 55.67
Item5 = 45.60
ItemTotal = Item1 + Item2 + Item3 + Item4 + Item5
ItemTax = 0.07
ItemTotalCost = ItemTotal * ItemTax


print(f"Subtotal: {ItemTotal: .2f}")
print(f"Tax: {ItemTax * ItemTotal: .2f}")
print(f"Total Cost: {ItemTotal + ItemTotalCost: .2f}")


Temperature = 30
ConversionToF = ((9/5)*Temperature) + 32
print(f"30 Degree Celsius is converted to {ConversionToF: .2f} Degrees Farenheit")


MealCost = float(input('What is the cost of your meal?: '))
CustomerTip = 0.20 * MealCost
CustomerTax = 0.0825 * MealCost
TotalMealCost = MealCost + CustomerTip + CustomerTax

print('PRICE BREAKDOWN')
print('-' * 20)
print(f"{'Your meal costs:':<15} ${MealCost:>6.2f}")
print(f"{'Your total tip is:':<15} ${CustomerTip:>6.2f}")
print(f"{'Your Tax is:':<15} ${CustomerTax:>6.2f}")
print('-' * 20)
print(f"{'Your total cost is:':<15} ${TotalMealCost:>6.2f}")