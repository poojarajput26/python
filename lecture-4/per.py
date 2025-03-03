# Taking percentage input from the user
percentage = float(input("Enter your percentage: "))
# Using if-else ladder to determine grade
if percentage >= 90 and percentage <= 100:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
elif percentage >= 40:
    grade = "E"
else:
    grade = "Fail"

print(f"Your grade is: {grade}")
