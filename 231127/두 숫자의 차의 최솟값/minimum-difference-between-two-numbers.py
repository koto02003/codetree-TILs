n = int(input())
list1 = list(map(int, input().split()))
min1 = 100
for i in range(n - 1):
    if list1[i + 1] - list1[i] < min1:
        min1 = list1[i + 1] - list1[i]

print(min1)