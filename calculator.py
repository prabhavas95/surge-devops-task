def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
    else:
        print("Cannot divide by zero")

    print("Are both values equal?", a == b)


calculator(10, 5)
def calculator(a, operator, b):
    if operator == "+":
        print("Result:", a + b)
    elif operator == "-":
        print("Result:", a - b)
    elif operator == "*":
        print("Result:", a * b)
    elif operator == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operator")

    if a == b:
        print("Both values are equal")
    elif a > b:
        print("First value is greater")
    else:
        print("First value is less")


a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

calculator(a, operator, b)