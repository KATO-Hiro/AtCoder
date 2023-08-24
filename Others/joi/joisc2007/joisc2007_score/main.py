# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    d = defaultdict(list)

    for i in range(n):
        si = int(input())
        d[si].append(i)

    # print(d)
    ans = [-1] * n
    rank = 1

    for keys in sorted(d.keys(), reverse=True):
        ids = d[keys]

        for id in ids:
            ans[id] = rank

        rank += len(ids)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
