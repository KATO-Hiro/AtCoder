# -*- coding: utf-8 -*-


# See:
# https://github.com/not522/ac-library-python/blob/master/atcoder/math.py
def floor_sum(n: int, m: int, a: int, b: int) -> int:
    ans = 0

    if a >= m:
        ans += (n - 1) * n * (a // m) // 2
        a %= m

    if b >= m:
        ans += n * (b // m)
        b %= m

    y_max = (a * n + b) // m
    x_max = y_max * m - b

    if y_max == 0:
        return ans

    ans += (n - (x_max + a - 1) // a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)

    return ans


def main():
    import sys
    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        ni, mi, ai, bi = map(int, input().split())
        print(floor_sum(ni, mi, ai, bi))


if __name__ == '__main__':
    main()
