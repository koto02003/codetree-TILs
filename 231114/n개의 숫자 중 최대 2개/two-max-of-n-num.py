n = int(input())
arr = list(map(int, input().split()))

maxNum1 = arr[0]
maxNum2 = arr[1]


for i in range(2, n):
    if maxNum1 < arr[i]:
        maxNum1 = arr[i]
    elif maxNum2 < arr[i]:
        maxNum2 = arr[i]

print(maxNum1, maxNum2)