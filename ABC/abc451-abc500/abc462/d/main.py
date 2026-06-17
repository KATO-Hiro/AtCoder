# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n, d = map(int, input().split())
    size = 10**6 + 10
    c = [0] * size

    for _ in range(n):
        si, ti = map(int, input().split())

        if si + d > ti:
            continue

        c[si] += 1
        c[ti - d + 1] -= 1

    acc = list(accumulate(c))
    ans = 0

    for i in range(1, size):
        m = acc[i]
        ans += m * (m - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
