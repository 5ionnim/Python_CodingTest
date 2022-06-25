#15904 UCPC는 무엇의 약자일까?
from collections import deque
line = deque(list(input()))
UCPC = ['U','C','P','C']
tag = True
for c in UCPC:
    t = False
    while line:
        if c == line.popleft():
            t = True
            break
    if t:
        continue
    tag = False
    break
if tag:
    print("I love UCPC")
else :
    print("I hate UCPC")