# Import the random library and have a look at the function gauss() which gives back a random float number. 
# Which parameters are required? Write a function gaussian_distribution() that returns a list of 1000 random numbers 
# with a mean of 100 and a standard deviation of 10. Invoke this function.

# For the resulting list calculate and print the mean and the standard deviation using the respective functions 
# from the statistics library. Re-run the program and observe, if the values change.


import random
import statistics

def gaussian_distribution():
    return [random.gauss(100, 10) for _ in range(1000)]

data = gaussian_distribution()
mean_value = statistics.mean(data)
std_dev_value = statistics.stdev(data)

print("Mean:", mean_value)
print("Standard Deviation:", std_dev_value)