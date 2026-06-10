# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = [int(input()) for _ in range(n)]

    d = defaultdict(list)

    for i, ai in enumerate(a):
        d[ai].append(i)

    pos = 0
    ans = [0] * n

    while pos < n:
        color = a[pos]
        last = d[color][-1]

        for j in range(pos, last + 1):
            ans[j] = color

        pos = last + 1

    for ans_i in ans:
        print(ans_i)


if __name__ == "__main__":
    main()
