# Greet the user before asking about a purchase
print("Welcome to Simon's Hardware Shop! Let's work on your order.")

# Ask if customer wants to buy any wiring
wire_q = str(input("Would you like to buy any wiring (yes/no)? "))

if wire_q == "yes":
    wire_num = float(input("How many feet of wiring would you like to buy? "))
    # Less than 10 feet of wiring costs $3.00 per foot
    if wire_num < 10.00:
        wire_price = 3.00 * wire_num
    # At least 10 feet but less than 20 feet costs $2.80 per foot
    elif wire_num >= 10.00 and wire_num < 20.00:
        wire_price = 2.80 * wire_num
    # At least 20 feet costs $2.60 per foot
    else:
        wire_price = 2.60 * wire_num
else:
    # If customer does not want to buy any wiring, it costs them nothing
    wire_price = 0
    if wire_q != "no":
        print("Oops! Looks like a typo. We’ll treat that as a no.")
print()

# Ask if customer wants to buy any light bulbs
bulb_q = str(input("Would you like to buy any light bulbs (yes/no)? "))
if bulb_q == "yes":
    bulb_num = float(input("How many light bulbs would you like to buy? "))
    # Fewer than 12 bulbs costs $1.00 each
    if bulb_num < 12.00: 
        bulb_price = 1.00 * bulb_num
    # At least 12 but fewer than 24 bulbs costs $0.95 each
    elif bulb_num >= 12.00 and bulb_num < 24.00:
        bulb_price = 0.95 * bulb_num
    # At least 24 bulbs costs $0.92 each
    else:
        bulb_price = 0.92 * bulb_num
else:
     # If customer does not want to buy any bulbs, it costs them nothing
    bulb_price = 0
    if bulb_q != "no":
        print("Oops! Looks like a typo. We’ll treat that as a no.")
print()

# Ask if customer wants to buy any paint
paint_q = str(input("Would you like to buy any paint (yes/no)? "))
if paint_q == "yes":
    paint_num = float(input("How many cans of paint would you like to buy? "))
    # Fewer than 5 cans costs $5.00 each
    if paint_num < 5.00:
        paint_price = 5.00 * paint_num
     # At least 5 but fewer than 10 cans costs $4.90 each
    elif paint_num >= 5.00 and paint_num < 10.00:
        paint_price = 4.90 * paint_num
     # At least 10 cans costs $4.80 each
    else:
        paint_price = 4.80 * paint_num
else:
     # If customer does not want to buy any paint, it costs them nothing
    paint_price = 0
    if paint_q != "no":
        print("Oops! Looks like a typo. We’ll treat that as a no.")
print()

# Sum the customer's total price
total = wire_price + bulb_price + paint_price

# Output the total price at check out
print("Your final total is", round(total,2), "dollars.\nThanks for visiting!")