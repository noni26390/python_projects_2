# Calculator with menu...

def calculator():
    print("Welcome to Python Calculator!")

    print("Choose operation:")

    print("1. Addition")

    print("2. Subtraction")

    print("3. Multiplication")

    print("4. Division")


    choice = int(input("Enter your choice (1-4): "))

    print()

    a = float(input("Enter your first numeric value: "))
    
    b = float(input("Enter your second numeric value: "))

    if choice == 1:
        print(f"{a} + {b} = {a + b}")

    elif choice == 2:
        print(f"{a} - {b} = {a - b}")

    elif choice == 3:
        print(f"{a} × {b} = {a * b}")

    elif choice == 4:
        if b != 0:
            print(f"{a} ÷ {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid choice! Please select a number between 1 and 4.")

# Call the function
calculator()
