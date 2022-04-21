#1789 수들의 합 
num = int(input())
count = 1

while True:
    if (num - count) <= count:
        break
    num -= count
    count += 1

print(count)