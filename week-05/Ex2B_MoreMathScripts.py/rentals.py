# Van rentals
import math

Passengers = int(input("How many people are going?: "))
VanLimit = 15
CostPerVan = 250
VansNeeded = math.ceil(Passengers/VanLimit)
TotalCost = CostPerVan * VansNeeded
PerPassenger = TotalCost/Passengers

print(f"The trip will cost: ${TotalCost: .2f}")
print(f"The vans needed will be: {VansNeeded: .2f}")
print(f"Each passenger should pay: ${PerPassenger: .2f}")

"""
Test your script with 38 tourists. Now do some separate calculations to check your
work:
a) How much money did your script say you had to charge per person? $19.74 per person
b) If you multiply that out, how much did you collect? $750.12 is what i got
c) How much were the vans? We needed 3 vans and each van was 250
d) Why do you have leftover money? We had leftover money because we went over the price
"""







