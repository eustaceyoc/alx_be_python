# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")  # Print '*' without a newline
    print()  # Move to the next row
    row += 1  # Increment row counter
