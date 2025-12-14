# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ans = (0, 0)

    for base in range(1, 10):
        number = base

        for digit in range(1, n + 1):
            if number % m == 0:
                ans = max(ans, (digit, base))

            number *= 10
            number += base
            number %= m

    if ans == (0, 0):
        print(-1)
    else:
        print(str(ans[1]) * ans[0])


if __name__ == "__main__":
    main()
