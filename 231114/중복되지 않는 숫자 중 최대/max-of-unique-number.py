n = int(input())
m = list(map(int, input().split()))
no = True
m.sort(reverse=True)

for i in range(0,n):
    if m.count(m[i]) == 1:
        big = m[i]
        no = False
        print(big)
        break
        
if no == True:
    print(-1)