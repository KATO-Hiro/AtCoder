# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, w = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    ans = 0

    for pattern in product([0, 1], repeat=n):
        summed_a, summed_b = 0, 0

        for pi, (ai, bi) in zip(pattern, ab):
            if pi == 0:
                continue

            summed_a += ai
            summed_b += bi

        if summed_b > w:
            continue

        ans = max(ans, summed_a)

    print(ans)


if __name__ == "__main__":
    main()
