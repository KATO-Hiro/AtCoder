# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = defaultdict(int)

    for _ in range(q):
        qi = list(map(str, input().split()))

        if qi[0] == "1":
            x, y = qi[1], qi[2]
            d[x] = int(y)
        else:
            x = qi[1]
            print(d[x])


if __name__ == "__main__":
    main()
