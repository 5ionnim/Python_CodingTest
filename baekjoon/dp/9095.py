#9095 1, 2, 3 더하기 (점화식 찾는 문제)
caseNum = int(input())
cases = [int(input()) for _ in range(caseNum)]
def tobBottom(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else :
        return tobBottom(num - 1) + tobBottom(num - 2) + tobBottom(num - 3)

for c in cases:
    print(tobBottom(c))
    
    
    
