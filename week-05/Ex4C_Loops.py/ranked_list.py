favorite_foods = ["jollof rice", "suya", "ramen", "tacos", "jerk chicken"]

for rank, food in enumerate(favorite_foods, 1):
    line = str(rank) + ". " + food
    if rank == 1:
        line = line + " <- top pick!"
    print(line)