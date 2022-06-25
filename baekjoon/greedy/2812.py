#2812 크게 만들기
N, K = map(int, input().split())
nums = list(input())
stack, dNum = [], K
for i in range(N):
    while stack and dNum and stack[-1]<nums[i]:
        stack.pop()
        dNum-=1
    stack.append(nums[i])
print(''.join(stack[:N-K]))
            