#1967 트리의 지름
import sys 
sys.setrecursionlimit(100000)

nodeNum = int(input())
edgeList = [[] for _ in range(nodeNum)]
maxLen = 0
for i in range(nodeNum - 1):
    a, b, c = map(int, input().split())
    edgeList[a-1].append([b - 1, c])

def search_tree(node):
    global edgeList, maxLen
    res = [0, 0]
    for s in edgeList[node]:
        b, c = s
        res.append(c+search_tree(b))
    res.sort(reverse = True)
    maxLen = max(maxLen, res[0] + res[1])
    return res[0]
        
search_tree(0)
print(maxLen)
    