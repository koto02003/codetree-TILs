n, m = map(int, input().split())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    if i == m:
        count += 1

print(count)