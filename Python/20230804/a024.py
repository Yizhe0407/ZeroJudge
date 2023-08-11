# def find_GCD(a, b):
#     common_factor = []
#     for i in range(1, max(a, b) + 1):
#         if max(a, b) % i == 0:
#             if min(a, b) % i == 0:
#                 common_factor.append(i)
#     return max(common_factor)


# a, b = map(int, input().split())
# print(find_GCD(a, b))
def find_GCD(a, b):
    while b:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
print(find_GCD(a, b))
