n , m = map(int,input().split())
prices = list(map(int,input().split()))
bestAffaire = 0
carryMax = 0
prices.sort()

for price in prices:
    if price < 0  and carryMax < m:
        bestAffaire += price
        carryMax += 1
        
print(abs(bestAffaire))