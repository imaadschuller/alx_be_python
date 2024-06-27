# Prompt the user for the size of pattern

size = int(input("Enter the size of the pattern (positive integer): "))

# Draw the pattern using nested loops
row = 0
while row < size:
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    print()  # Move to the next line after each row is printed
    row += 1

