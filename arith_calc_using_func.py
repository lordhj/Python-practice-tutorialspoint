def add(num1, num2):
    return num1+num2
def sub(num1, num2):
    return num1-num2
def multiply(num1, num2):
    return num1*num2
def divide(num1, num2):
    return num1/num2
def modulus(num1, num2):
    return num1%num2
def exp(num1, num2):
    return num1**num2
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
print("SUM: ", add(num1, num2))
print("DIFFERENCE: ", sub(num1, num2))
print("PRODUCT: ", multiply(num1, num2))
print("DIVISION: ", divide(num1, num2))
print("MODULUS: ", modulus(num1, num2))
print("EXPONENT: ", exp(num1, num2))