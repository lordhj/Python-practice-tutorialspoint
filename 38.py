number = int(input("Please Enter any Number: "))
total = 0
for value in range(1, number + 1):
    total = total + value
average = total / number
print(total)
print(average)