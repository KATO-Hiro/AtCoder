# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    size = max(a) + 1
    s, t, u = [0] * size, [0] * size, [0] * size

    # n の倍数となる個数を前計算
    for ai in a:
        s[ai] += 1

    for d in range(1, size):
        for m in range(d, size, d):
            t[d] += s[m]

    for d in range(1, size):
        if t[d] < k:
            continue

        for m in range(d, size, d):
            u[m] = max(u[m], d)

    ans = list()

    for ai in a:
        ans.append(u[ai])

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
