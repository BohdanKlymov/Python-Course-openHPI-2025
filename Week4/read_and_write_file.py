# The file numbers.txt contains numbers. (Actually, the same numbers from the last exercise.) 
# There is exactly one number per line. 
# Read the numbers from the file and write only the even numbers into a new file named even_numbers.txt. 
# Again, there should be one number per line. 
# The order of the numbers shall be unchanged. 
# To indicate that the program is finished, print the following output: "List of even numbers created!"

numbers = []

with open("numbers.txt", "r") as read_file:
    for number in read_file:
        numbers.append(int(number.strip()))

with open("even_numbers.txt", "w") as write_file:
    for number in numbers:
        if number % 2 == 0:
            write_file.write(str(number) + "\n")

print("List of even numbers created!")