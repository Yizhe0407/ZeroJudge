# method 1
try:
    while True:
        year = int(input())
        if (year % 4 == 0 and year % 100) or year % 400 == 0:
            print('閏年')
        else:
            print('平年')
except (EOFError, ValueError):
    pass

# method 2
from sys import stdin
for read in stdin:  # 反覆讀取
    year = int(read)  # 將讀取內容(字串)轉整數
    # 閏年判斷式
    if (year % 4 == 0 and year % 100) or year % 400 == 0:
        print('閏年')
    # 否則
    else:
        print('平年')
