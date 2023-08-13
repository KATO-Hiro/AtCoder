# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = list(input().rstrip())
    c = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ci in enumerate(c):
        d[ci].append(i)

    ans = [""] * n

    for i in range(1, m + 1):
        size = len(d[i])

        for j in range(size):
            before, after = d[i][j], d[i][(j - 1) % size]
            ans[before] = s[after]

    print("".join(ans))


if __name__ == "__main__":
    main()
