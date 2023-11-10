inputList = list(map(int, input().split()))
list1 = []
sum = 0

for i in range(100):
    inp = inputList[i]
    if inp == 0:
        break
    list1.append(inp)

for i in range(-1, -4, -1):
    sum += list1[i]

print(sum)