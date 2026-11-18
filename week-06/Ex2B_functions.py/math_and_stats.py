import random
import math
import statistics

vals_1_100 = range(1, 101)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)
radius = random.randint(3, 10)
pi = math.pi

# Experimenting with a subset of integers 1-100
sample_sum = sum(vals_sample)
sample_average = statistics.mean(vals_sample)
sample_median = statistics.median(vals_sample)

# Experimenting with a superset of 200 values, integers 1-100
choices_average = statistics.mean(vals_choices)
choices_median = statistics.median(vals_choices)
choices_mode = statistics.mode(vals_choices)
choices_standard_deviation = statistics.stdev(vals_choices)
choices_variance = statistics.variance(vals_choices)

# Modeling a random circle:
area = pi * radius ** 2
area_rounded_up = math.ceil(area)
area_rounded_down = math.floor(area)

# Display values for 1 - 100 range
print("_Experimenting with a subset of integers 1-100:")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", sample_average)
print("Median of 75 sample values:", sample_median)

print("\n")

# Display values for 200
print("_Experimenting with a superset of 200 values, integers 1-100:")
print("Average of 200 values:", choices_average)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_standard_deviation)
print("Variance of 200 values:", choices_variance)

print("\n")

# Display the circle portion
print("_Modeling a random circle:")
print(
    "Radius =", radius,
    ", area =", area_rounded_up,
    "(rounded up to the nearest integer)"
)

print(
    "Radius =", radius,
    ", area =", area_rounded_down,
    "(rounded down to the nearest integer)"
)