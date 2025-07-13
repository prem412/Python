firstNumebr = float(input("Enter first number: "))
operation = input("Enter (+, -, *, /): ")
secondNumber = float(input("Enter second number: "))

if operation == "+":
    print("Result:", firstNumebr + secondNumber)
elif operation == "-":
    print("Result:", firstNumebr - secondNumber)
elif operation == "*":
    print("Result:", firstNumebr * secondNumber)
elif operation == "/":
    if secondNumber != 0:
        print("Result:", firstNumebr / secondNumber)
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operator")

    
