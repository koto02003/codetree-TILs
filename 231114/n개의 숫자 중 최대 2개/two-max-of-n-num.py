n = int(input())
arr = list(map(int, input().split()))
if arr[0] > arr[1]:
    maxNum1 = arr[0]
    maxNum2 = arr[1]
else:
    maxNum1 = arr[1]
    maxNum2 = arr[0]

for i in range(2, n):
    if maxNum1 < arr[i]:
        maxNum1 = arr[i]

for i in range(2, n):
    if maxNum2 < arr[i] and maxNum1 != arr[i]:
        maxNum2 = arr[i]

print(maxNum1, maxNum2)