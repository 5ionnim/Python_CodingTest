#10610 30 
nums = list(map(int, input()))
nums.sort(reverse = True)
if (nums[-1] == 0) & (sum(nums[0:-1])%3 == 0):
    print(''.join(map(str,nums)))
    
else:
    print(-1)