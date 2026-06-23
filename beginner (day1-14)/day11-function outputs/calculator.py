def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": divide
}

def calculator():

    while True:

        first = float(input("What's the first number? "))

        for op in operations:
            print(op)

        should_continue = True

        while should_continue:

            choose = input("Choose operation (+, -, *, /): ")
            sec = float(input("Enter second number: "))

            calculation_function = operations[choose]
            answer = calculation_function(first, sec)

            print(f"{first} {choose} {sec} = {answer}")

            continue_calc = input(
                f"Type 'y' to continue calculating with {answer}, or 'n' to stop: "
            ).lower()

            if continue_calc == "y":
                first = answer
            else:
                should_continue = False

        restart = input(
            "Do you want to start a new calculation? (y/n): "
        ).lower()

        if restart != "y":
            print("Goodbye!")
            break


calculator()