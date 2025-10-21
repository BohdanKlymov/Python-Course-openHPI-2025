# The expression formula discriminant is called the discriminant. 
# Using the discriminant makes it is easy to check the number of solutions for a given quadratic equation:

# If the discriminant is 0, the quadratic equation has exactly one real solution.
# If the discriminant is > 0, the quadratic equation has two real solutions.
# If the discriminant is < 0, the quadratic equation has two complex solutions.
# Write a program that asks the user for the numbers a, b and c. The program should then print out how many solutions the quadratic equation has.


a = int(input("Please enter the value of a: "))
b = int(input("Please enter the value of b: "))
c = int(input("Please enter the value of c: "))

result = b * b - 4 * a * c

if result == 0:
    print("The quadratic equation has 1 real solution.")
elif result > 0:
    print("The quadratic equation has 2 real solutions.")
else:
    print("The quadratic equation has 2 complex solutions.")