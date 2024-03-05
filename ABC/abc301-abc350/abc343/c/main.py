# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    x_max = 10**6
    ans = 1

    for x in range(1, x_max + 1):
        k = x**3

        if k > n:
            break

        s = str(k)
        t = s[::-1]

        if s == t:
            ans = max(ans, k)

    print(ans)


if __name__ == "__main__":
    main()
