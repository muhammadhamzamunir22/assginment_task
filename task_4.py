
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def mod(a, b):
    return a % b

def div(a, b):
    return a / b


while True:
    a = float(input("Enter 1st Number: "))
    b = float(input("Enter 2nd Number: "))

    op = input("Enter operation (+, -, *, /, %): ")

    if op == "+":
        print(add(a, b))
    elif op == "-":
        print(sub(a, b))
    elif op == "*":
        print(mul(a, b))
    elif op == "/":
        if b != 0:
            print(div(a, b))
        else:
            print("Cannot divide by zero")
    elif op == "%":
        if b != 0:
            print(mod(a, b))
        else:
            print("Cannot calculate modulo by zero")
    else:
        print("Invalid operation")

    again = input("Again (Yes/No): ")

    if again.lower() != "yes":
        break