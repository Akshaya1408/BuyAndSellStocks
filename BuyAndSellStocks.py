def max_profit(A):
    if not A or len(A) == 1:
        return 0

    min_price = A[0]
    max_profit = 0

    for price in A:
        min_price = min(min_price, price)
        pot_profit = price - min_price
        max_profit = max(max_profit, pot_profit)

    return max_profit

A = list(map(int,input().split()))
print(max_profit(A))  
