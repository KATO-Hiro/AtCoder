# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    ans = 0

    for ai, bi in zip(a, b):
        diff = ai - bi
        diff = max(0, diff)

        c.append(diff)

    total = 0

    for j in range(n):
        total += c[j]

        if j >= m:
            total -= c[j - m]

        ans = max(ans, total)

    print(ans)


if __name__ == "__main__":
    main()
