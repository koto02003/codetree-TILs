n = int(input())
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0]
inp = list(map(int, input().split()))
for i in inp:
    arr[i - 1] += 1

for i in arr:
    print(i)