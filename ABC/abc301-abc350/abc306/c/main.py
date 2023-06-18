# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i, ai in enumerate(a, 1):
        d[ai].append(i)

    c = list()

    for key, value in d.items():
        vi = sorted(value)[1]

        c.append((vi, key))

    ans = list()

    for _, i in sorted(c):
        ans.append(i)

    print(*ans)


if __name__ == "__main__":
    main()
