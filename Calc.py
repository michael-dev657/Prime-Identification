def calculator():
    a = int(input("Enter your first number: "))
    b = int(input("Enter your second number: "))
    operation = input("Enter your desired operation: ")
    if operation == "addition":
        result = a + b
    elif operation == "subtraction":
        result = a - b
    elif operation == "multiplication":
        result = a * b
    elif operation == "division":
        result = a / b
    else:
        print("Invalid operation!")
    print(f"The answer is: {result}")
calculator()