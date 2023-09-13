# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, m = map(int, input().split())
    xyz = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for f1, f2, f3 in product([-1, 1], repeat=3):
        candidates = list()

        for xi, yi, zi in xyz:
            candidates.append(xi * f1 + yi * f2 + zi * f3)

        candidates = sorted(candidates, reverse=True)
        ans = max(ans, sum(candidates[:m]))

    print(ans)


if __name__ == "__main__":
    main()
