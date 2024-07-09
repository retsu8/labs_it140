import sys

# Get change for changing
change = int(input())

# Check if there is any change
if change == 0:
    print("No change")
    sys.exit()

# Handle Dollars
dollars = int(change / 100)
if dollars > 1:
    print(f"""{dollars} Dollars""")
elif dollars == 1:
    print(f"""{dollars} Dollar""")

# Remove the dollar/s
if dollars:
    change = change - 100 * dollars

# Handle the quearters
quarters = int(change / 25)
if quarters > 1:
    print(f"""{quarters} Quarters""")
elif quarters == 1:
    print(f"""{quarters} Quarter""")

# Remove the quarter/s
if quarters:
    change = change - 25 * quarters


# Handle the dimes
dimes = int(change / 10)
if dimes > 1:
    print(f"""{dimes} Dimes""")
elif dimes == 1:
    print(f"""{dimes} Dime""")

if dimes:
    change = change - 10 * dimes

# Hanlde the Nickels
nickels = int(change / 5)
if nickels > 1:
    print(f"""{nickels} Nickels""")
elif nickels == 1:
    print(f"""{nickels} Nickel""")

# Remove the Nickel/s
if nickels:
    change = change - 5 * nickels

# Whats left is pennies
if change > 1:
    print(f"""{change} Pennies""")
elif change == 1:
    print(f"""{change} Penny""")
