number = float(input("Enter a number: "))  # I converted the input to float to handle decimal numbers

if number > 0:
    print("The number is positive.")
elif number == 0:  # Used == for equality comparison
    print("The number is zero.")
else:  # Remove condition from else statement
    print("The number is negative.")
    