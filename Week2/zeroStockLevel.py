# In this exercise you are going to simulate a sales and operations planning using the zero stock level strategy. 
# Write a Python program that asks the user to enter the following data:

# An initial stock level for a product
# The number of month(s) to plan
# The planned sales quantity for each month
# Based on this data, calculate the required production quantity as follows:

# If the sales quantity is smaller than the stock level of the previous month, the production quantity is 0
# If the sales quantity is larger than the stock level of the previous month, the production quantity is this difference

initial_stock = int(input("Please enter an initial stock level: "))

num_months = int(input("Please enter the number of month(s) to plan: "))

planned_sales = []

for month in range(1, num_months + 1):
    sales = int(input(f"Please enter the planned sales quantity for month {month}: "))
    planned_sales.append(sales)

stock = initial_stock
production_quantities = []

for sales in planned_sales:
    if sales <= stock:
        production = 0
    else:
        production = sales - stock
    production_quantities.append(production)

    stock = stock + production - sales

print("\nThe resulting production quantities are:")
for month, qty in enumerate(production_quantities, start=1):
    print(f"Production quantity month {month} - {qty}")