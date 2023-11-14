n, q = map(int, input().split())

elements = list(map(int, input().split()))

for i in range(q):
    find = -1
    question = list(input().split())
    
    if question[0] == '1':
        print(elements[int(question[1]) - 1])
    elif question[0] == '2':
        for j in range(len(elements)):
            if elements[j] == int(question[1]):
                find = j + 1
                break
        if find == -1:
            print(0)
        else:
            print(find)
    elif question[0] == '3':
        for z in range(int(question[1]), int(question[2]) + 1): 
            print(elements[z - 1], end = ' ')
        print()