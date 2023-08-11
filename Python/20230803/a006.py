a, b, c = map(int, input().split())
number = b ** 2 - 4 * a * c
if number > 0:
    ans1 = int((-b + number ** 0.5) / (2 * a))
    ans2 = int((-b - number ** 0.5) / (2 * a))
    print(f"Two different roots x1={ans1} , x2={ans2}")
elif number == 0:
    ans = int((-b + number ** 0.5) / (2 * a))
    print(f"Two same roots x={ans}")
else:
    print("No real root")
