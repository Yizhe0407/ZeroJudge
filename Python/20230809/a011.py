import re


def count_words_in_line(line):
    words = re.findall(r'\b[a-zA-Z]+\b', line)
    return len(words)


# 讀取輸入並處理每行
while True:
    try:
        line = input()
        if not line:
            break
        word_count = count_words_in_line(line)
        print(word_count)
    except EOFError:
        break
