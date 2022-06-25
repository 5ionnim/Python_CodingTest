#4195 친구 네트워크
testCase = int(input())
res=[]
for t in range(testCase):
    F = int(input())
    li = [[] for _ in range(F)]
    di = dict()
    for f in range(F):
        a, b = input().split()
        if a in di.keys() and b in di.keys():
            if di[a]<di[b]:
                k = di[b]
                for l in li[k]:
                    di[l] = di[a]
                    li[di[a]].append(l)
                li[k]=[]
            elif di[a]>di[b]:
                k = di[a]
                for l in li[k]:
                    di[l] = di[b]
                    li[di[b]].append(l)
                li[k]=[]
        elif a in di.keys() and b not in di.keys():
            di[b] = di[a]
            li[di[a]].append(b)
        elif b in di.keys() and a not in di.keys():
            di[a] = di[b]
            li[di[b]].append(a)
        else:
            di[a] = f
            di[b] = f
            li[f].append(a)
            li[f].append(b)
        res.append(len(li[min(di[a],di[b])]))
for r in res:
    print(r)