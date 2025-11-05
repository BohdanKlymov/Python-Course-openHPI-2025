# There is a file secret.txt, which contains one character per line. 
# There is a second file key.txt, which contains two lines with one number per line (the number could have several digits). 
# The first number col represents the number of columns of a grid, the second number row represents the number of rows of the grid.

# The characters of the first file should now be filled into this grid. 
# Take the characters one by one and fill them into a string until the string contains col characters. 
# Append the string to a list. Then create a new string the same way. Continue, until the number of strings is equal to row. 
# Now, write all the strings into a file public.txt. Open the the file and check the content.

# Please note: When programming your solution in CodeOcean, files created by your program will not be visible. 
# If you want to check the content of those files, 
# we suggest to let your code run on your machine (e.g. in a Jupyter Notebook) and check the content of the files there.

with open("key.txt", "r") as key_file:
    col = int(key_file.readline().strip())
    row = int(key_file.readline().strip())

chars = []
with open("secret.txt", "r") as secret_file:
    for ch in secret_file:
        chars.append(ch.strip())  # remove newline

grid = []
index = 0
for r in range(row):
    line = ""
    for c in range(col):
        line += chars[index]
        index += 1
    grid.append(line)

with open("public.txt", "w") as public_file:
    for line in grid:
        public_file.write(line + "\n")

print("public.txt created!")