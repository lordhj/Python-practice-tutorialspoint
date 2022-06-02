num = int(input("Enter: "))
reverse = 0
temp = num
while (temp>0):
    rem = temp% 10
    reverse = reverse * 10 + rem
    temp = temp//10
if num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")