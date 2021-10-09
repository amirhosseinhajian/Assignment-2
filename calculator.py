import math

print("welcom to calculator.")
while True:
    print("choose an operator: ")
    print("+")
    print("-")
    print("*")
    print("/")
    print("sin")
    print("cos")
    print("tan")
    print("cot")
    print("log")
    print("exit")
    op = input()
    if op == "exit":
        break
    elif op == "+" or op == "-" or op == "*" or op =="/":
        a = int(input("enter the first number: "))
        b = int(input("enter the seccond nunber: "))
        if op == '+':
            result = a + b
        elif op == "-":
            result = a - b
        elif op == '/':
            if b == 0:
                print("can not division by zero.")
                result = "infinity"
            else:
                result = a / b
        elif op == '*':
            result = a * b
        print(f"The result is: {result}")
    elif op == "sin" or op == "cos" or op == "tan" or op == "cot":
        a = int(input("enter the number: "))
        if op == "sin":
            result = math.sin(a)
        elif op == "cos":
            result = math.cos(a)
        elif op == "tan":
            result = math.tan(a)
        elif op == "cot":
            result = 1 / math.tan(a)
        print(f"The result is: {result}")
    elif op == "log":
        a = int(input("enter the number: "))
        b = int(input("enter the number base: "))
        result = math.log(a, b)
        print(f"The result is: {result}")
    else:
        print("the input operator is wrong.")