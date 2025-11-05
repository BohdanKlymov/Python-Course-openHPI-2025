# The file invoice_data.txt contains raw data for an invoice. More precisely, each line contains

#     the name of an item
#     how many items are bought
#     the unit price of the item

# The three values are separated by a single whitespace. Prepare a beautified output of the file which contains

#     the name of the item formatted with 15 characters
#     the number of units with 3 digits
#     the price per item with 7 digits, 2 digits after the decimal point
#     the total price (number of items * price per item) with 8 digits in total, 2 digits after the decimal point

# If there are two lines with the following content “Apple 5 0.99” and “Cherry 2 11.99”, 
# then the beautified output should look as follows:

# Apple           15   0.99   14.85
# Cherry           2  11.99   23.98

data = []

with open("invoice_data.txt", "r") as read_file:
    for line in read_file:
        item, qty, price = line.split()
        qty = int(qty)
        price = float(price)
        data.append((item, qty, price))

for item, qty, price in data:
    total = qty * price
    print(f"{item:<15}{qty:3d}{price:7.2f}{total:8.2f}")