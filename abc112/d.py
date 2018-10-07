# -*- coding: utf-8 -*-


def main():
    from math import sqrt

    n, m = map(int, input().split())
    ans = 1

    # See:
    # https://www.youtube.com/watch?v=CURWJ1Dr44A
    for k in range(1, int(sqrt(m)) + 1):
        if m % k != 0:
            continue

        if k * n <= m:
            ans = max(ans, k)

        b = m // k

        if b * n <= m:
            ans = max(ans, b)

    print(ans)


if __name__ == '__main__':
    main()
