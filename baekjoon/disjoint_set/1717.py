#1717 집합의표현
import sys
sys.setrecursionlimit(10**5)
def union(a, b):
    global nList
    sa = search(a)
    sb = search(b)
    k = min(sa, sb)
    nList[sa] = k
    nList[sb] = k
    
def search(a):
    global nList
    if a == nList[a]:
        return a
    nList[a] = search(nList[a])
    return nList[a]

n, m = map(int, input().split())
nList = [ x for x in range(n+1)]
res = []
for i in range(m):
    o, t, h = map(int, input().split())
    if o == 0:
        union(t, h)
    else :
        if search(t)==search(h):
            res.append('YES')
        else :
            res.append('NO')
for r in res:
    print(r)
