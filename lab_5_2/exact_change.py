def exact_change(input_val):
    """Determine exact change for input and return"""

    def process_change(input_v, value):
        """Handle redunt coin processing"""
        change = int(input_v / value)
        input_v -= change * value
        return change, input_v

    dollars = 0
    quarters = 0
    nickels = 0
    dimes = 0
    pennies = 0
    if input_val > 99:
        dollars, input_val = process_change(input_val, 100)
    if input_val > 24:
        quarters, input_val = process_change(input_val, 25)
    if input_val > 9:
        dimes, input_val = process_change(input_val, 10)
    if input_val > 4:
        nickels, input_val = process_change(input_val, 5)
    pennies = input_val
    return dollars, quarters, dimes, nickels, pennies


if __name__ == "__main__":
    """Main function handle user interaction, send to get exact_change"""
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val
    )
    if not num_dollars + num_quarters + num_dimes + num_nickels + num_pennies:
        print("no change")
    # Handle multiples for printing the change
    if num_dollars > 1:
        print(f"{num_dollars} dollars")
    elif num_dollars:
        print(f"{num_dollars} dollar")
    if num_quarters > 1:
        print(f"{num_quarters} quarters")
    elif num_quarters: 
        print(f"{num_quarters} quarter")
    if num_dimes > 1:
        print(f"{num_dimes} dimes")  
    elif num_dimes: 
        print(f"{num_dimes} dime")
    if num_nickels > 1:
        print(f"{num_nickels} nickels")
    elif num_nickels: 
        print(f"{num_nickels} nickel")
    if num_pennies > 1:
        print(f"{num_pennies} pennies")
    elif num_pennies: 
        print(f"{num_pennies} penny")
