# Using the library random create 10,000 random points inside the square. 
# That means generate 10,000 random pairs of values for x and y. 
# The random value must be between 0 and 1 in order for a point to be inside the square. 
# For each point check if x² + y² is < 1. If this is the case, then the point is within the circle. 
# Count the total number of points and the points which are in the circle. 
# Use these numbers to calculate π. Finally compare your calculated value of π with the value of π found in the math library. 
# Do this by printing the calculated value of π, the value from the math library as well as the difference.

# Below is an example execution of the program. Note that your values might be different.

#     Calculated value of π: 3.1396
#     Value of π from math library: 3.141592653589793
#     Difference: -0.0019926535897929476


import random
import math

inside = 0
total = 10000

for _ in range(total):
    x = random.random()
    y = random.random()
    if x*x + y*y < 1:
        inside += 1

pi_calc = 4 * inside / total

print("Calculated value of π:", pi_calc)
print("Value of π from math library:", math.pi)
print("Difference:", pi_calc - math.pi)