# -*- coding: utf-8 -*-


from calendar import c


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    rc = [tuple(map(int, input().split())) for _ in range(n)]
    r_min = min([ri for ri, _ in rc])
    r_max = max([ri for ri, _ in rc])
    c_min = min([ci for _, ci in rc])
    c_max = max([ci for _, ci in rc])

    inf = 10**18
    ans = inf

    for y in range(r_min, r_max + 1):
        for x in range(c_min, c_max + 1):
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
