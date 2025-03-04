# Take input from the user
num = int(input("Enter a number: "))
# Check if the number is prime
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  # Check up to the square root of num
        if num % i == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
