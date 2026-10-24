# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    q = int(input())
    d = defaultdict(int)
    id = 0
    ans = []

    for _ in range(q):
        si = input().rstrip()

        if si not in d:
            id += 1
            d[si] = id

        ans.append(d[si])

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
