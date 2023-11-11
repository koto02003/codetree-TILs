n = int(input())
arr = []
count = 0
i = n

while(True):
    arr.append(n)
    if(n % 5 == 0):
        count += 1
        if(count == 2):
            break
    n += i
    
for i in arr:
    print(i, end = ' ')