# Tiles
import math

Length = float(input("Whats the length of the room?: "))
Width = float(input("Whats the width of the room?: "))
TilesNeeded = Length * Width
IncreaseBy = 0.10 * TilesNeeded
TotalIncrease = TilesNeeded + IncreaseBy
TilesPerBox = 12
BoxesNeeded = math.ceil(TotalIncrease/TilesPerBox)

print(f"You need specifically: {TilesNeeded: .2f} amount of tiles")
print(f"But you actually need: {TotalIncrease: .2f} amount of tiles")
print(f"You also need approximately: {BoxesNeeded} boxes")



