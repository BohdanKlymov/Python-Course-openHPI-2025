# The file numbers.txt contains random integer numbers. 
# There is exactly one number per line. 
# Read the file and output the three biggest numbers

numbers = []

with open("numbers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        numbers.append(number)

numbers.sort(reverse=True)

for num in numbers[:3]:
    print(num)