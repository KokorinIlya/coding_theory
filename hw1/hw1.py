g = [
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0]
]


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

n = len(g)
m = len(g[0])
assert m == len(h_t)
k = len(h_t[0])


result = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        for z in range(m):
            result[i][j] += g[i][z] * h_t[z][j]
            result[i][j] %= 2

print(result)