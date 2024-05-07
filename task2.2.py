# Prompting the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Identifying the largest number among the three
if num1 > num2 and num1 > num3:
    largest = num1
elif num2 > num1 and num2 > num3:
    largest = num2
else:
    largest = num3

# Identifying the smallest number among the three
if num1 < num2 and num1 < num3:
    smallest = num1
elif num2 < num1 and num2 < num3:
    smallest = num2
else:
    smallest = num3

# Checking if two or all numbers are equal
if num1 == num2 and num1 == num3:
    print("All numbers are equal.")
elif num1 == num2:
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)
    print("The first and second numbers are equal.")
elif num1 == num3:
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)
    print("The first and third numbers are equal.")
elif num2 == num3:
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)
    print("The second and third numbers are equal.")
else:
    print("The smallest number is:", smallest)
    print("The largest number is:", largest)
    print("There are no equal numbers.")
