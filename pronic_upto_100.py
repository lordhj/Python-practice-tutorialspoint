for x in range(1, 100):
    for i in range(1, (x//2+1)):
        if i*(i+1) == x:
            print(x)