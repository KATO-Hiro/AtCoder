# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    d = 2 * (n - m)
    b, c = a[:d], a[d:]
    ans = 0

    for i in range(n - m):
        ans += (b[i] + b[-(i + 1)]) ** 2

    for ci in c:
        ans += ci**2

    print(ans)


if __name__ == "__main__":
    main()
