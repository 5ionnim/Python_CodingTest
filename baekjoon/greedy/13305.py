#13305 주유소 
minP = 1000000000
cityNum = int(input())
distances = list(map(int, input().split()))
cityPrice = list(map(int, input().split()))
rePrices = []
for p in range(cityNum - 1):
    if (minP > cityPrice[p]):
        minP = cityPrice[p]
    rePrices.append(minP * distances[p])
print(sum(rePrices))
    

