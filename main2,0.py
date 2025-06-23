#Simple calculator program

valid_operator = ["+", "-", "*", "/"] # Operators that are used for math

while True:
    operator = input("Please enter your operator: (+ - * /), or 'q' to quit: ")

    if operator == 'q':
        print("Thank you for playing!")
        break

    if operator not in valid_operator:
        print("Invalid operator. Please try again.")
        continue  

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Сalculation
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by zero!")
            continue
        result = num1 / num2

    if result.is_integer():
        print(f"Result: {int(result)}")  # If whole — transform to int
    else:
        print(f"Result: {round(result, 4)}")  # Other — leave as float
