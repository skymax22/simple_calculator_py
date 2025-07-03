 #calculator

def calculate(num1, num2, operator):
    if operator == "+":
        return round(num1 + num2, 3) # addition
    elif operator == "-":
        return round(num1 - num2, 3) # subtraction
    elif operator == "*":
        return round(num1 * num2, 3) # multiplication
    elif operator == "/":
        if num2 == 0:
            print("You cannot divide by zero!")
            return None
        else:
            return round(num1 / num2, 3) # division
    elif operator == "%":
        if num2 == 0:
            print("You cannot use modulus with zero!")
            return None
        else:
            return round(num1 % num2, 3) # modulus
    elif operator == "**":
        return round(num1 ** num2, 3) # exponent
    elif operator == "//":
        if num2 == 0:
            print("You cannot perform integer division by zero!")
            return None
        else:
            return round(num1 // num2, 3) # integer division
    else:
        return None

valid_operator = {"+", "-", "*", "/", "//", "**", "%"} # Operators that are used for math

while True:
    operator = input("Please enter your operator (+ - * / // ** %), or 'q' to quit: ").strip()
    operator = operator.replace(" ", "")

    if operator.strip().lower() == "q":
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

    result = calculate(num1, num2, operator)

    if result is not None:
        if result == int(result):
            print(f"Result: {int(result)}")  # If whole — transform to int
        else:
            print(f"Result: {round(result, 3)}")  # Other — leave as float
    else:
        pass
