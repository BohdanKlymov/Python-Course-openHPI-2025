# The file numbers.txt contains random integer numbers. 
# There is exactly one number per line. 
# Read the file and output the three biggest numbers

with open("numbers.txt", "r") as file:
    nums_list = []
    for line in file:
        line = line.strip()
        nums_list.append(line)
    
    max_number1 = max(nums_list)
    
    print(max_number1)
    nums_list.remove(max_number1)
    
    max_number2 = max(nums_list)
    
    print(max_number2)
    nums_list.remove(max_number2)
    
    max_number3 = max(nums_list)
        
    print(max_number3)
    nums_list.remove(max_number3)