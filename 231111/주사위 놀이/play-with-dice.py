dice = [0, 0, 0, 0, 0, 0]
inp = list(map(int, input().split()))
for i in inp:
    dice[i - 1] += 1

for i in range(1, 7):
    print(f"{i} - {dice[i - 1]}")