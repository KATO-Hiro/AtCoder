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

    r_center = (r_min + r_max) // 2
    c_center = (c_min + c_max) // 2
    ans = inf

    for y in range(r_center - 2, r_center + 3):
        for x in range(c_center - 2, c_center + 3):
            candidates = 0

            for yi, xi in rc:
                dy = abs(y - yi)
                dx = abs(x - xi)
                d = min(dy, dx)

                candidate = dy + dx - d
                candidates = max(candidates, candidate)

            ans = min(ans, candidates)

    print(ans)


if __name__ == "__main__":
    main()
