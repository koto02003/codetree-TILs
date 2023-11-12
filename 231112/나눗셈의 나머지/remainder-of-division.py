a, b = map(int, input().split())
re = [0, 0, 0, 0, 0, 0, 0, 0, 0]
result = 0
while(a >= 1):
    a /= b
    re[int(a % b) - 1] += 1


for i in re:
    if(i != 0):
        result += i * i


print(result)