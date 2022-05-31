cost = int(input("Enter the actual price: "))
sale = int(input("Enter the sales amount: "))
if cost>sale:
    result = "Loss"
    diff = cost-sale
else:
    result = "Profit"
    diff = sale-cost
print("You have a", result, "of", diff)