# get the food charge from the user
food_cost = float(input("Enter the charge for the food: $"))

# calculate  the tip (18%) and tax (7%)
tip = food_cost * 0.18
tax = food_cost* 0.07

# calculate total amount
total = food_cost + tip + tax

# display the results
print(f"Food Charge: ${food_cost:.2f}")
print(f"Tip (18%):   ${tip:.2f}")
print(f"Tax (7%):    ${tax:.2f}")
print(f"Total:       ${total:.2f}")