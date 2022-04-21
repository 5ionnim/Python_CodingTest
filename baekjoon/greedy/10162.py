#10162 전자레인지 
dishTimes = int(input())
nums = [300, 60, 10]
buttonNums = [0, 0, 0]
for n in range(3):
    nt = dishTimes//nums[n]
    dishTimes -= nt * nums[n]
    buttonNums[n] = nt

if (dishTimes == 0):
    print(buttonNums[0],buttonNums[1],buttonNums[2])
else:
    print(-1)
    