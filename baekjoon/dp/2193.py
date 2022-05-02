#2193 이친수
num = int(input())
numList = [[0,0] for _ in range(num)]
numList[0] = [0, 1]
for i in range(1, num):
    numList[i][0] = numList[i-1][0] + numList[i-1][1]
    numList[i][1] = numList[i-1][0]
print(numList[num-1][0] + numList[num-1][1])