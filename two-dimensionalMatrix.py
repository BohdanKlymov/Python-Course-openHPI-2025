# Write a program that lets the user input a two-dimensional matrix (Hint: you could use a list of lists to store the matrix). 
# The program should first ask the user how many rows and columns the matrix should contain. 
# Next, the program should ask the user for the elements of the matrix. Your program should read the values from the user row by row. 
# If, for example, the matrix has the dimension 2 by 3, the values should be read as follows:

# First row, first value
# First row, second value
# First row, third value
# Second row, first value
# Second row, second value
# Second row, third value
# Finally, the program should calculate and print the sums of the values in each row.

rows = int(input("Please enter the number of rows in the matrix: "))
cols = int(input("Please enter the number of columns in the matrix: "))

matrix = []

print("Enter the matrix values:")

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input("Value: "))
        row.append(value)
    matrix.append(row)

for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Sum of row: {row_sum}")