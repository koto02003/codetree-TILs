n = int(input())
inputList = list(map(int, input().split()))
new_list = []

for i in inputList:
    if(i % 2 == 0):
        new_list.append(i)

for i in new_list:
    print(i, end=' ')