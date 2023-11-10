inputList = list(map(int, input().split()))
evenSum = 0
oddSum = 0
for i in range(1, 11):
    if i % 2 == 0:
        evenSum += inputList[i - 1]
    else:
        oddSum += inputList[i - 1]

if evenSum > oddSum:
    print(evenSum - oddSum)
else:
    print(oddSum - evenSum)