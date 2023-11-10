inputList = list(map(int, input().split()))

for i in inputList:
    if i % 3 == 0:
        print(inputList[i - 1])
        break