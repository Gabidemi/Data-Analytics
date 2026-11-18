import random

products = [
    "Laptop",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Webcam",
    "Headset",
    "Docking Station",
    "USB Hub",
    "Desk Lamp",
    "Surge Protector"
]

# 1 Product
product_of_the_day = random.choice(products)
print("Product of the Day:", product_of_the_day)

# 3 different products
survey_products = random.sample(products, 3)
print("Products for the usability survey:", survey_products)

# Randomized order
random.shuffle(products)
print("Randomized product list:", products)

# randomint
transaction_count = random.randint(50, 300)
print("Daily transaction count:", transaction_count)