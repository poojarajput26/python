# 1. Right-Angled Triangle Pattern:
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()


# 2. Pyramid Pattern:
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i * 2):
        print("*", end="")
    print()
