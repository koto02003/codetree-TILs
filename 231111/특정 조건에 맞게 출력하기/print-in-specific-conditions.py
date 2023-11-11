inp= list(map(int, input().split()))
result = []

for i in inp:
    if(i == 0):
        break
    if(i % 2 == 0):
        i /= 2
    else:
        i += 3
    result.append(int(i))

for i in result:
    print(i, end = ' ')