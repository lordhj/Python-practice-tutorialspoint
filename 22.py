pri = int(input("Enter the principal amount "))
roi = float(input("Enter the rate of interest "))
t = int(input("Enter the time period in years: "))
ci = pri*(1+roi/100)**t
print("Future compund interest ",ci)
print("compund interest for principal ", ci-pri)