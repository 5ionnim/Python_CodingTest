#1339 단어 수학 
wordNum = int(input())
words = []
alphasD = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0
}

nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(wordNum):
    words.append(list(input()))

for word in words:
    for i in range(len(word)):
        alphasD[word[i]] += 10 ** (len(word) - (i+1))
res = 0

resList = list(alphasD.values())
resList.sort(reverse = True)
for i in range(10):
    res += resList[i] * nums[i]
print(res)