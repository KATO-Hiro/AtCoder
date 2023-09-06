# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for _ in range(m):
        xi, yi = map(int, input().split())
        d[xi] = yi

    for i, ai in enumerate(a, 2):
        t -= ai

        if t <= 0:
            print("No")
            exit()

        t += d[i]

    print("Yes")


if __name__ == "__main__":
    main()
