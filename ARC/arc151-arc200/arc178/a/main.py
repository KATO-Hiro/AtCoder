# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    if 1 in a or n in a:
        print(-1)
        exit()

    p = [i for i in range(n + 1)]

    for ai in a:
        p[ai], p[ai + 1] = p[ai + 1], p[ai]

    print(*p[1:])


if __name__ == "__main__":
    main()
