#11047 동전 0 

coinNum, totalC = map(int, input().split())
kOCoin = []
coinSum = 0
for i in range(coinNum):
    kOCoin.append(int(input()))

kOCoin.reverse()
for k in kOCoin:
    kSum = totalC//k
    totalC = totalC - kSum * k
    coinSum = coinSum + kSum
print(coinSum)
