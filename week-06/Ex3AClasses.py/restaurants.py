class Restaurant:

    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.food_type}.")

    def restaurant_open(self):
        print(f"{self.restaurant_name} is open.")


restaurant1 = Restaurant("Lagos Kitchen", "Nigerian food")
restaurant2 = Restaurant("Pasta Palace", "Italian food")
restaurant3 = Restaurant("Taco House", "Mexican food")

restaurant1.describe_restaurant()
restaurant1.restaurant_open()

restaurant2.describe_restaurant()
restaurant2.restaurant_open()

restaurant3.describe_restaurant()
restaurant3.restaurant_open()