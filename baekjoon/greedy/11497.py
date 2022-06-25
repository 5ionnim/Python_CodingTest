#11497 통나무 건너뛰기
from collections import deque
T = int(input())
res = []
for t in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    L = deque(L)
    a = L.popleft()
    b = L.popleft()
    c = L.popleft()
    r = max(c-a, c-b, b-a)
    tList = [a, c, b]
    for i in range(len(L)):
        d = L.popleft()
        if i%2==0:
            r = max(r, d - tList[2])
            tList = [tList[1], d, tList[2]]
        else: 
            r = max(r, d - tList[0])
            tList = [tList[0], d, tList[1]]
    res.append(r)
for r in res:
    print(r)