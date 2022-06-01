first = 0
second = 1
num = int(input("Upto what: "))
print(first)
print(second)
for i in range(2, num+1):
    third = first + second
    print(third)
    first, second = second, third