#2748 피보나치 수 2
num = int(input())
fiboList = [0]*(num+1)
fiboList[1] = 1
def fibonacci(n):
    global fiboList
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif fiboList[n] == 0:
        fiboList[n] = fibonacci(n-1) + fibonacci(n-2)
    return fiboList[n]
print(fibonacci(num))