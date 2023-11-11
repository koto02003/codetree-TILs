n1, n2 = map(int, input().split())
arr = []
arr.append(n1)
arr.append(n2)


for i in range(2, 10):
    n = arr[i - 1] + arr[i - 2]
    if n >= 10:
        n %= 10
    arr.append(n)


for i in arr:
    print(i, end = ' ')