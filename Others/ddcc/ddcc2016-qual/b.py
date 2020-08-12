# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    r, n, m = map(int, input().split())
    large_r = r ** 2
    ans = 0

    for i in range(n + m):
        first = max(i - m, 0)
        second = min(i, n)

        ans1 = sqrt(large_r - abs(r - (2 * r * first / n)) ** 2)
        ans2 = sqrt(large_r - abs(r - (2 * r * second / n)) ** 2)
        ans += max(ans1, ans2)

    print(ans * 2)


if __name__ == '__main__':
    main()
