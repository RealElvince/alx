# Challenge 1: total harvest in Kilograms
total_kgs_wheat_harvest = 2050
total_kgs_potato_harvest = 3600

total_kgs_harvest = total_kgs_wheat_harvest + total_kgs_potato_harvest

print("Total harvest in Kilograms:",total_kgs_harvest)

# Challenge 2:Total Expenses in dollars
seed_expense = 650
labour_expense = 3070

total_expenses_dollars = seed_expense + labour_expense
print("Total expenses in dollars:",total_expenses_dollars)

# Challenge 3 : Calculate total revenue in dollars and print the results
price_per_kg_wheat = 2
price_per_kg_potato = 1.4

total_revenue_dollars = (total_kgs_wheat_harvest*price_per_kg_wheat) + (total_kgs_potato_harvest*price_per_kg_potato)
print("Total revenue in dollars:",total_revenue_dollars)

# challenge 4:Calculate total profit in dollars
total_profit_dollars = total_revenue_dollars - total_expenses_dollars
print("Total profit in dollars:",total_profit_dollars)