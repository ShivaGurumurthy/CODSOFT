def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Dividing a value by zero is not permitted. Please try again with a different value other than '0'..."
    else:
        return a / b

def mod(a, b):
    return a % b

def expo(a, b):
    return a ** b

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Modulus")
    print("6.Exponent")
    choice = int(input("Enter the specified operation's number from above: "))
    if 1 <= choice <= 6:
        a = int(input("Enter a value for a:"))
        b = int(input("Enter a value for b:"))
        if choice == 1:
            print(f"{a} + {b} = {add(a, b)}")
        elif choice == 2:
            print(f"{a} - {b} = {sub(a, b)}")
        elif choice == 3:
            print(f"{a} * {b} = {mul(a, b)}")
        elif choice == 4:
            print(f"{a} / {b} = {div(a, b)}")
        elif choice == 5:
            print(f"{a} % {b} = {mod(a, b)}")
        elif choice == 6:
            print(f"{a} ** {b} = {expo(a, b)}")
    else:
        print("Wrong input.... Please try again with a different and valid input...")   