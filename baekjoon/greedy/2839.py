#2839 설탕 배달 

num = int(input())
fEnvel = 0
tEnvel = 0

mfNum = num//5

for i in range(mfNum,-1, -1):
    left = num - i*5
    mtNum = left//3
    if ((i*5 + mtNum*3) == num):
        fEnvel = i
        tEnvel = mtNum
        break

if ((fEnvel + tEnvel) > 0):
    print(fEnvel + tEnvel)
else:
    print(-1)
