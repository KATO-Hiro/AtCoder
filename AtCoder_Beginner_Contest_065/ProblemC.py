'''input
100000 100000
530123477

2 2
8

3 2
12

1 8
0

'''

# -*- coding: utf-8 -*-

# AtCoder Beginner Contest
# Problem C

if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    diff = abs(n - m)
    n_factorial = 1
    m_factorial = 1
    large_number = 10 ** 9 + 7

    for i in range(1, n + 1):
        n_factorial = (n_factorial * i) % large_number

    for k in range(1, m + 1):
        m_factorial = (m_factorial * k) % large_number

    rate = 0

    if diff == 1:
        rate = 1
    elif diff == 0:
        rate = 2

    print(((n_factorial * m_factorial * rate) % large_number))
