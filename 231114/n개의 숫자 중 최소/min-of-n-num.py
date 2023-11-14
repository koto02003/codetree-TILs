n = int(input())
arr = list(map(int, input().split()))
minNum = arr[0]
count = 1

for i in range(1, n):
    if minNum > arr[i]:
        minNum = arr[i]
        count = 1
    elif minNum == arr[i]:
        count += 1

print(minNum, count)