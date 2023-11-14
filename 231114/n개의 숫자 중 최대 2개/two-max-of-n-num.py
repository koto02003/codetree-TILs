n = int(input())
arr = list(map(int, input().split()))
maxNum = arr[0]
maxIndex = -1
maxIndex2 = -1
for i in range(1, n):
    if maxNum < arr[i]:
        maxIndex = i
        maxNum = arr[i]

maxNum = arr[0]
for i in range(1, n):
    if i == maxIndex:
        continue
    if maxNum < arr[i]:
        maxIndex2 = i
        maxNum = arr[i]

print(arr[maxIndex], arr[maxIndex2])