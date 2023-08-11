try:
    while True:
        binary = []
        figure = int(input())
        while figure:
            if figure % 2 == 0:
                binary.append('0')
            else:
                binary.append('1')
            figure //= 2
        binary.reverse()
        print(''.join(binary))
except EOFError:
    pass
