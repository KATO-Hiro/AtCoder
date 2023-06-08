# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    q = int(input())
    d = defaultdict(int)

    for _ in range(q):
        qi = list(map(str, input().split()))

        if qi[0] == "1":
            x, y = qi[1:]
            d[x] = int(y)
        else:
            print(d[qi[1]])


if __name__ == "__main__":
    main()
