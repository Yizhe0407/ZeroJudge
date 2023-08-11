from collections import Counter


def generate_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
    return primes


def prime_factorization(number, primes):
    factors = []
    for prime in primes:
        if prime * prime > number:
            break
        while number % prime == 0:
            factors.append(prime)
            number //= prime
    if number > 1:
        factors.append(number)
    return factors


limit = 10000
primes = generate_primes(limit)
input_number = int(input("请输入一个数字："))
factors = prime_factorization(input_number, primes)

number_counts = Counter(factors)
output_parts = []
for number, count in number_counts.items():
    if count >= 2:
        output_parts.append(f'{number}^{count}')
    else:
        output_parts.append(str(number))
formatted_output = " * ".join(output_parts)
print(formatted_output)

# from collections import Counter


# def is_prime():
#     primes = []
#     for j in range(2, 10000):
#         check = 1
#         if j == 2:
#             primes.append(j)
#             continue
#         if j % 2 == 0:
#             check = 0
#         for k in range(3, int(j**0.5) + 1, 2):
#             if j % k == 0:
#                 check = 0
#         if check == 1:
#             primes.append(j)
#     return primes


# primes = is_prime()
# figure = int(input())
# i = 0
# num = 0
# factor = []

# while figure != 1:
#     if figure % primes[i] == 0:
#         factor.append(primes[i])
#         figure /= primes[i]
#     else:
#         i += 1

# output_parts = []
# number_counts = Counter(factor)
# for number, count in number_counts.items():
#     if count >= 2:
#         output_parts.append(f'{number}^{count}')
#     else:
#         output_parts.append(str(number))
# formatted_output = " * ".join(output_parts)
# print(formatted_output)
