#11726 2*n 타일링
num = int(input())
def dfs(a):
    global num
    if a == 1:
        return 1
    alist = [0]*(num+1)
    alist[1] = 1
    alist[2] = 2
    for i in range(3,num+1):
        alist[i] = alist[i-1] + alist[i-2]
    return alist[num]
print(dfs(num)%10007)
    