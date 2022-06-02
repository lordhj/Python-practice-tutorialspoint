num = int(input("Enter number: "))
for i in range(1, (num//2+1)):
    if i*(i+1) == num:
        print("Pronic")
    else:
        print("Not Pronic")