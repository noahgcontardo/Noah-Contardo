def divide(a, b):
    c = a / b
    print(c)

def multiply(a, b):
    c = a / b
    print(c)

def subtract(a, b):
    c = a - b
    print(c)

def add(a, b):
    c = a + b
    print(c)

def user_selection(user_input, a, b):
    if user_input.lower() not in ["add", "subtract", "multiply", "divide"]:
        print("invalid input please type either: add, subtract, multiply or divide")
        return
    match user_input.lower():
        case "add":
            add(a, b)
        case "subtract":
            subtract(a, b)
        case "multiply":
            multiply(a, b)
        case "divide":
            divide(a, b)
    
def main():
    print("welcome to the calculator app, this will take 2 inputs and allow you to chose a mathematical operation to perform on them, keep in mind they are in order")
    a = int(input("please proide the first integer to perform your one step arithmetic with: "))
    b = int(input("please proide the second integer to perform your one step arithmetic with: "))
    operation_selection = input("please select an operation by typing \'add, subtract, multiply or divide\'")
    user_selection(operation_selection, a, b)


main()