# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop to print asterisks in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to next line after printing the row
    row += 1