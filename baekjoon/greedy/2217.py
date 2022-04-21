#2217 로프 
ropeNum = int(input())
ropes = []
maxW = 0
for i in range(ropeNum):
    ropes.append(int(input()))
ropes.sort()
for n in range(ropeNum):
    if (maxW < ropes[n] * (ropeNum - n)):
        maxW = ropes[n] * (ropeNum - n)

print(maxW)
    
