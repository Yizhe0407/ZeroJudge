while True:
    try:
        a, b = map(int, input().split())
        if a < 2 ** 63 and b < 2 ** 63:
            print(abs(a - b))
        else:
            continue
    except EOFError:
        break
