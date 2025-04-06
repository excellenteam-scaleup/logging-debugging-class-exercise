# Use pdb to do the following instructions -
# 0. Run the code. Calculate the total revenue of the orders that were not canceled and
# figure out the right output value
# 1. import the library
# 2. set up a breakpoint somewhere in the code
# 3. run the code through the terminal
# 4. Use help on one of the commands
# 5. Show the next 10 lines on the screen
# 6. Show lines 1 to 30 on the screen using one of pdb's command
# 7. Iterate through each iteration of the list comprehension in filter_valid_orders, and print the
# value of order each time.
# 8. Run this script in a way that will immediately enter debugging
# 9. Add a breakpoint while in debug mode
# 10. continue the execution of the code to that breakpoint
# 11. disable the breakpoint
# 12. Run a python expression while debugging - sum two variables
# 12. Find the 2 bugs using pdb

def process_orders(orders):
    valid_orders = filter_valid_orders(orders)
    total = calculate_total_revenue(valid_orders)
    return {
        "valid_orders": len(valid_orders),
        "total_revenue": total
    }


def filter_valid_orders(orders):
    # Filters out orders that were canceled
    return [order for order in orders if order.get("canceled", False)]


def calculate_total_revenue(orders):
    total = 0
    for order in orders:
        for item in order["items"]:
            total = item["price"] * item["quantity"]
    return total


orders = [
    {
        "id": 1,
        "canceled": False,
        "items": [
            {"name": "Book", "price": 12.99, "quantity": 2},
            {"name": "Pen", "price": 1.50, "quantity": 3}
        ]
    },
    {
        "id": 2,
        "canceled": True,
        "items": [
            {"name": "Notebook", "price": 5.00, "quantity": 5}
        ]
    },
    {
        "id": 3,
        "canceled": False,
        "items": [
            {"name": "Bag", "price": 50.00, "quantity": 1}
        ]
    }
]

print(process_orders(orders))
