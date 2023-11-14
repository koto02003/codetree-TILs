arr = ['L', 'E', 'B', 'R', 'O', 'S']
key = input()
find = -1
for i in range(len(arr)):
    if arr[i] == key:
        find = i

if find == -1:
    print("None")
else:
    print(find)