# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10**18
    r_min, r_max, c_min, c_max = inf, -inf, inf, -inf
    rc = [tuple(map(int, input().split())) for _ in range(n)]

    for ri, ci in rc:
        r_min = min(r_min, ri)
        r_max = max(r_max, ri)
        c_min = min(c_min, ci)
        c_max = max(c_max, ci)

    r = r_max - r_min
    c = c_max - c_min

    print((max(r, c) + 1) // 2)


if __name__ == "__main__":
    main()
