# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    p = list(map(int, input().split()))
    d = defaultdict(list)

    for i, pi in enumerate(p):
        d[pi].append(i)

    r = 1
    ans = [-1] * n

    for key in sorted(d.keys(), reverse=True):
        ids = d[key]
        k = len(ids)

        for id in ids:
            ans[id] = r

        r += k

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
