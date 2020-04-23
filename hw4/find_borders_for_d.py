import math


def c(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def check_hamming(n, k, d):
    t = (d - 1) // 2
    total_sum = 0
    for i in range(t + 1):
        total_sum += c(n, i)
    return total_sum <= 2 ** (n - k)


n = 25
k = 17

cur_d = 1
while True:
    if not check_hamming(n, k, cur_d):
        print(cur_d - 1)  # 4
        break
    else:
        cur_d += 1


def check_hilbert(n, k, d):
    total_sum = 0
    for i in range(d - 1):
        total_sum += c(n - 1, i)
    return total_sum < 2 ** (n - k)


cur_d = 1
while True:
    if not check_hilbert(n, k, cur_d):
        print(cur_d - 1)
        break
    else:
        cur_d += 1