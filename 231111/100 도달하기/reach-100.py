n = int(input())
arr = [1, n]
i = 0

for i in range(2, 100):
    inp = arr[i - 2] + arr[i - 1]
    arr.append(inp)
    if(inp > 100):
        break

for i in arr:
    print(i, end= ' ')