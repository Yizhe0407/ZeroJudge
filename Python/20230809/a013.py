import re

figures = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
           'IV': 4, 'IX': 9, 'IL': 49, 'IC': 99, 'ID': 499, 'IM': 999,
           'VL': 45, 'VC': 95, 'VD': 455, 'VM': 995, 'XD': 490, 'XM': 990,
           'XL': 40, 'XC': 90, 'LD': 450, 'LM': 950, 'CD': 400, 'CM': 900,
           'II': 2, 'III': 3, 'VI': 6, 'VII': 7, 'VIII': 8, 'MM': 2000,
           'VV': 10, 'XX': 20, 'LL': 100, 'CC': 200, 'DD': 1000, }
figures = dict(sorted(figures.items(), key=lambda x: x[1], reverse=True))


def calculate(nums):
    sum1 = []
    sum2 = []
    e = 0
    f = 0
    num1, num2 = nums.split()
    num1 = re.findall(r'[A-Z]{2}', num1)
    num2 = re.findall(r'[A-Z]{2}', num2)
    for a in num1:
        sum1.append(figures[a])
    for b in num2:
        sum2.append(figures[b])
    for c in sum1:
        e += c
    for d in sum2:
        f += d
    sum = abs(e - f)
    return sum


def split_number(number):
    if number == 0:
        return 'ZERO'
    else:
        digits = list(str(number))
        results = [int(digit) * 10**(len(digits)-i-1)
                   for i, digit in enumerate(digits)]
        u = []
        for key, val in figures.items():
            for result in results:
                if val == result:
                    u.append(key)
                    del results[0]
                    continue
        r = ''.join(i for i in u)
        return r


while True:
    nums = input()
    if nums == '#':
        break
    else:
        print(split_number(calculate(nums)))
