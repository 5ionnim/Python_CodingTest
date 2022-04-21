#1026 보물 

nNum = int(input())
numsA = list(map(int, input().split()))
numsB = list(map(int, input().split()))
total = 0

numsA.sort(reverse = True)
numsB.sort()

for i in range(nNum):
    total = total + numsA[i] * numsB[i]

print(total)