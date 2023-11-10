inputList = list(map(int, input().split()))

for i in range(10):
    if inputList[i] % 3 == 0:
        print(inputList[i - 1])
        break