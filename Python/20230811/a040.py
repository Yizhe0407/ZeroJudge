def find_armstrong_number(low_range, high_range):
    armstrong_number = []
    for nums in range(low_range, high_range + 1):
        value = [int(num) for num in str(nums)]
        power = len(value)
        power_sum = sum(val ** power for val in value)
        if power_sum == nums:
            armstrong_number.append(nums)
    if not armstrong_number:
        print('none')
    else:
        print(' '.join(map(str, armstrong_number)))


low_range, high_range = map(int, input().split())
if 0 < low_range < high_range <= 1000000:
    find_armstrong_number(low_range, high_range)
