state = [0, 0, 0, 0]
for i in range(3):
    check = 3
    cold, tem = input().split()
    if(cold == 'Y'):
        check -= 1
    if(int(tem) >= 37):
        check -= 2
    
    state[check] += 1


for i in state:
    print(i, end = ' ')
if(state[0] >= 2):
    print("E")