def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


while True:
    try:
        x = int(input())
        if is_prime(x):
            print("質數")
        else:
            print("非質數")
    except EOFError:
        break
