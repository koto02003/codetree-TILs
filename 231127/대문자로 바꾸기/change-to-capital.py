n = 5
arr = [
    list(input().split())
    for _ in range(n)
]

for i in range(n):
    for j in range(3):
        print(arr[i][j].upper(), end = ' ')
    print()