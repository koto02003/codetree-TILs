inp = list(map(int, input().split()))
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in inp:
    if(i == 0):
        break
    i /= 10
    arr[int(i - 1)] += 1

for i in range(9, -1, -1):
    print(f"{(i + 1) * 10} - {arr[i]}")