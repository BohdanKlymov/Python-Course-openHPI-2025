# Write a Python program that prints the numbers from 1 to 100. 
# If the number is dividable by 3 print Fizz, if the number is dividable by 5 print Buzz instead of the number. 
# If the number is dividable by 3 and 5 print FizzBuzz.

# Below is the output of the program for the first 15 numbers:

for i in range(1, 101):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")

    elif i % 5 == 0:
        print("Buzz")

    else:
        print(i)