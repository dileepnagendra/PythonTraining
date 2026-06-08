#Arranging Coins

def arrangingcoins(n):
    row = 1
    while n>=row:
        n = n-row
        row += 1
    return row-1
n=int(input("Enter Number:"))
print(arrangingcoins(n))