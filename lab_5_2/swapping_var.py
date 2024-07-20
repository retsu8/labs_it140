def swap_values(user_val1, user_val2):
    """Build print swap values function"""
    return user_val2, user_val1


# Swap values of input
if __name__ == "__main__":
    # Collect user input
    var_1 = int(input())
    var_2 = int(input())
    val1, val2 = swap_values(var_1, var_2)
    print(val1, val2)
