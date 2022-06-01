max = int(input("Enter max value: "))
total_odd = 0
total_even = 0
for i in range(1, max+1):
    if i%2==0:
        total_even = total_even+i
    else:
        total_odd = total_odd + i
print("Even sum : ", total_even)
print("Odd Sum: ", total_odd)