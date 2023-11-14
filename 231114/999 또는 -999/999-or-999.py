arr = list(map(int, input().split()))
minNum = 1000
maxNum = -1000

for i in arr:
    if i == -999 or i == 999:
        break
    if i > maxNum:
        maxNum = i
    if i < minNum:
        minNum = i

print(maxNum, minNum)