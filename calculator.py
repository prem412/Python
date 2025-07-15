def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b if b != 0 else "Cannot divide by zero"

a = int(input("Enter first number: "))
op = input("Enter operation (+, -, *, /): ")
b = int(input("Enter second number: "))

if op == '+':
    result = add(a, b)
    print("Result:", result)
elif op == '-':
    result = sub(a, b)
    print("Result:", result)
elif op == '*':
    result = mul(a, b)
    print("Result:", result)
elif op == '/':
    result = div(a, b)
    print("Result:", result)
else:
    result = "Invalid operation"
    print("Result:", result)



