def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[None for _ in range(n)] for _ in range(m)]

    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    return transposed


h = [
    [0, 0, 0, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
]

h_t = transpose(h)


def multiply(vect, mat):
    n = 1
    m = 10
    k = 4
    result = [0 for _ in range(k)]

    for j in range(k):
        for z in range(m):
            result[j] += vect[z] * mat[z][j]
            result[j] %= 2
    return result


ss = [
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
]

es = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 1]
]

right = 0
for cur_s, cur_e in zip(ss, es):
    if multiply(cur_e, h_t) != cur_s:
        print(cur_s, cur_e, multiply(cur_e, h_t))
    else:
        right += 1

print(right)
