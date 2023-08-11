num = int(input())
r = []

for i in range(num):
    r = list(map(int, input().split()))
    if r[1] - r[0] == r[-1] - r[-2]:
        r.append(r[-1] + (r[1] - r[0]))
    elif r[1] / r[0] == r[-1] / r[-2]:
        r.append(r[-1] * (r[1] / r[0]))
    for i in range(len(r)):
        print(int(r[i]), end=' ')
    print()
