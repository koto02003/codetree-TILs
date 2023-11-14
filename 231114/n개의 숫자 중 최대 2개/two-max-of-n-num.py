n = int(input())
arr = list(map(int, input().split()))
maxNum = arr[0]
maxIndex = 0

for i in range(1, n):
    if maxNum < arr[i]:
        maxIndex = i
        maxNum = arr[i]
        print(maxIndex)

print(arr[maxIndex], end= ' ')
maxNum = arr[0]
for i in range(1, n):
    if i == maxIndex:
        continue
    if maxNum < arr[i]:
        maxIndex = i
        maxNum = arr[i]

print(arr[maxIndex])