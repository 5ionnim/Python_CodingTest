#1049 기타줄
cuttedNum, brandNum = map(int, input().split()) 
nFA = cuttedNum//6
nFP = cuttedNum%6

minNFA = 10000
minNFP = 1000
for i in range(brandNum):
    aFL, pFL = map(int, input().split())
    minnerA = min([aFL, pFL*6])
    
    if (minNFA > minnerA):
        minNFA = minnerA
    if (minNFP > pFL):
        minNFP = pFL
print(nFA*minNFA + (minNFA if minNFA<=nFP*minNFP else nFP*minNFP))
    
    