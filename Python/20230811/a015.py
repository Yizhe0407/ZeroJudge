
def matrix_flip(rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for row in range(rows):
        matrix[row] = list(map(int, input().split()))

    rows, cols = cols, rows
    flip_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for j in range(rows):
        for k in range(cols):
            flip_matrix[j][k] = matrix[k][j]

    for row in range(rows):
        for col in range(cols):
            print(flip_matrix[row][col], end=' ')
        print()


try:
    while True:
        rows, cols = map(int, input().split())
        if rows < 100 and cols < 100:
            matrix_flip(rows, cols)
except EOFError:
    pass
