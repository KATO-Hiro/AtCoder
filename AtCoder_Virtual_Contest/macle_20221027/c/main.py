# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())

    if k == 0:
        print(n ** 2)
        exit()

    ans = 0

    for bi in range(k + 1, n + 1):
        p, q = divmod(n, bi)

        cycle = max(0, bi - k)
        ans += p * cycle + max(0, q - k + 1)

    print(ans)


if __name__ == "__main__":
    main()
