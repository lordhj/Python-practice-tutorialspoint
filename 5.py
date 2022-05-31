num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
oper = input("Enter operation(+, -, *, /, %): ")
if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    if num2 == 0:
        print("Zero Division Error")
elif oper =='%':
    print(num1%num2)