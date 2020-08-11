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
large_number = 10 ** 9 + 7


def factorial(number: int) -> int:
    value = 1

    for i in range(1, number + 1):
        value = (value * i) % large_number
    return value


if __name__ == '__main__':
    n, m = list(map(int, input().split()))
    diff = abs(n - m)
    result = factorial(min(n, m))

    # See:
    # https://beta.atcoder.jp/contests/abc065/submissions/1654425
    if diff == 1:
        rate = 1
        print(((result * result * max(n, m) * rate) % large_number))
    elif diff == 0:
        rate = 2
        print(((result * result * rate) % large_number))
    else:
        print(0)
