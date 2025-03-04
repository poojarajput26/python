# 4) Print this pattern using nested for Loop : 


# Number of rows for the pattern
rows = 5
# Outer loop for number of rows
for i in range(1, rows + 1):
    # Inner loop for printing stars in each row
    for j in range(i):
        print("*", end=" ")  # Print a star, and stay on the same line
    print()  # Move to the next line after each row
