arr = list(map(int, input().split()))
maxNum = 0
for i in arr:
    if maxNum < i:
        maxNum = i

print(maxNum)