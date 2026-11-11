# Distance
import math

Distance = float(input("Input your x1: "))
Distance2 = float(input("input your x2: "))
Distance3 = float(input("Input your y1: "))
Distance4 = float(input("Input your y2: "))

DistanceFormulaA = ((Distance2 - Distance)**2) + ((Distance4 - Distance3)**2)
DistanceFormulaB = math.sqrt(DistanceFormulaA)

print(f"The distance between them is: {DistanceFormulaB: .2f}")