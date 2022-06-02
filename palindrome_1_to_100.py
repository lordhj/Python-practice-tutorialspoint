for i in range(1, 101):
    reverse = 0
    temp = i
    while (temp>0):
        rem = temp% 10
        reverse = reverse * 10 + rem
        temp = temp//10
    if i == reverse:
        print(i)
        