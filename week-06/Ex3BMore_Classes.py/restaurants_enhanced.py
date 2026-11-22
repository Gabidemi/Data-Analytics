class Restaurant:

    def __init__(self, restaurant_name, food_type):
        self.restaurant_name = restaurant_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.food_type}.")

    def restaurant_open(self):
        print(f"{self.restaurant_name} is open.")

    def add_num_served(self):
        customers = int(input("How many customers served today? "))
        self.number_served = self.number_served + customers

    def print_num_served(self):
        print(f"{self.restaurant_name} has served {self.number_served} customers")

    def customer_rating(self):
        rating = input(
            "How would you rate your experience today "
            "on a scale of 1-5 (5 being excellent)? "
        )

        while rating not in ["1", "2", "3", "4", "5"]:
            print("Please enter a whole number from 1 to 5.")
            rating = input("Enter your rating: ")

        rating = int(rating)
        self.customer_ratings.append(rating)

        average = sum(self.customer_ratings) / len(self.customer_ratings)

        print(
            f"Your rating was {rating}. "
            f"The average rating for this restaurant is {average:.2f}"
        )


restaurant1 = Restaurant("Lagos Kitchen", "Nigerian food")
restaurant2 = Restaurant("Pasta Palace", "Italian food")
restaurant3 = Restaurant("Taco House", "Mexican food")

restaurants = [restaurant1, restaurant2, restaurant3]

for restaurant in restaurants:
    restaurant.describe_restaurant()
    restaurant.restaurant_open()

    restaurant.print_num_served()

    restaurant.add_num_served()
    restaurant.add_num_served()
    restaurant.add_num_served()

    restaurant.print_num_served()

    restaurant.customer_rating()
    restaurant.customer_rating()
    restaurant.customer_rating()

    print()