def calculator():

# Print welcome message
 print("Welcome to Basic Calculator!")

 while True:
    # Get first number
    try:
        num1 = input("\nEnter first number: ")
        if num1.lower() == 'q':
            print("Thank you for using Basic Calculator!")
            break
        num1 = float(num1)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Get operation
    operation = input("Enter operation (+, -, *, /): ")
    if operation.lower() == 'q':
        print("Thank you for using Basic Calculator!")
        break
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operation. Please try again.")
        continue

    # Get second number
    try:
        num2 = input("Enter second number: ")
        if num2.lower() == 'q':
            print("Thank you for using Basic Calculator!")
            break
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    # Perform calculation
    try:
        if operation == '+':
            result = num1 + num2
            print(f"\n{num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\n{num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\n{num1} * {num2} = {result}")
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero!")
                continue
            result = num1 / num2
            print(f"\n{num1} / {num2} = {result}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        continue

if __name__ == "__main__":
    calculator()