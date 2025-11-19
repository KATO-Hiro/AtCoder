# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    m = int(input())
    d = defaultdict(int)

    for y in range(m):
        x = (y**3) % m
        d[x] = y

    for i in range(m):
        ans = -1

        if i in d:
            ans = d[i]

        print(ans)


if __name__ == "__main__":
    main()
