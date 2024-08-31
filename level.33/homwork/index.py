lasha = input("enter an operator(+ - * / //): ")
num1 = float(input("enter the 1st number"))
num2 = float(input("enter the 2nd number"))

if lasha == "+":
    result = num1 + num2
    print(round(result, 3))
elif lasha == "-":
    result = num1 - num2
    print(round(result, 3))
elif lasha == "*":
    result = num1 * num2
    print(round(result, 3))
elif lasha == "//":
    result = num1 // num2
    print(round(result, 3))
elif lasha == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{lasha} is not a vaild operator ")
