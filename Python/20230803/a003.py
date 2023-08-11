M, D = map(int, input().split())

fortunes = {0: '普通', 1: '吉', 2: '大吉'}

S = (M * 2 + D) % 3
print(fortunes[S])
