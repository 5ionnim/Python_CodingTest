#11727 2×n 타일링 2
num = int(input())
initList = [1, 3]
for n in range(2, num):
    m = initList[n-2]*2 + initList[n-1]
    initList.append(m)
print(initList[num-1]%10007)