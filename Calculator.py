def Add():
    x = int(input("x: "))
    y = int(input("y: "))

    result = x + y
    print(f"{x} + {y} = {result}")

def Sub():
    x = int(input("x: "))
    y = int(input("y: "))

    result = x - y
    print(f"{x} - {y} = {result}")

def Multiply():

    x = int(input("x: "))
    y = int(input("y: "))

    result = x * y
    print(f"{x} x {y} = {result}")

def Divide():

    x = int(input("x: "))
    y = int(input("y: "))

    result = x // y
    print(f"{x} // {y} = {result}")


user_input = input(" ")

if user_input == "add":
    Add()

if user_input == "subtract":
    Sub()

if user_input == "multiply":
    Multiply()

if user_input == "divide":
    Divide()