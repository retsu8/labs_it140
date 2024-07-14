triangle_char = input("Enter a character:\n")
triangle_height = int(input("Enter triangle height:\n"))

# Make easy to read line indent here
print("")

# Print the triangle
for x in range(triangle_height):
    print((triangle_char + " ") * (x + 1))
