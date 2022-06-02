for i in range(1, 101): 
    digits = []
    dig = i
    while dig>0:
        dig_rem = dig%10
        digits.append(dig_rem)
        dig = dig//10
    tot = sum(digits)
    if i%tot ==0:
        print(i)