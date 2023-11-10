inputList = list(map(int, input().split()))
add = 0
avg = 0
for i in range(1, 11):
    if i % 2 == 0:
        add += inputList[i - 1]
    if i % 3 == 0:
        avg += inputList[i - 1]

avg /= 3

print("%d %.1f" %(add, avg))