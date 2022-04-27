#2720 세탁소 사장 동혁 
caseNum = int(input())
cases = [int(input()) for _ in range(caseNum)]
kind = [25, 10, 5, 1]
res = []
for c in cases:
    a = c
    r = ["0", "0", "0", "0"]
    for k in range(4):
        if a >= kind[k]:
            r[k] = str(a//kind[k])
            a = a%kind[k]
    res.append(" ".join(r))
for r in res:
    print(r)
        
    
    