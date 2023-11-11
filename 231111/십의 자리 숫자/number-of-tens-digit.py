inp = list(map(int, input().split()))
arr = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in inp:
    if(i == 0):
        break
    i /= 10
    arr[int(i)] += 1

for i in range(1, 10):
    print(f"{i} - {arr[i]}")