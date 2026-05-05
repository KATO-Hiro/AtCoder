# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n, k, d = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    patterns = product([0, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        summed_a, summed_b = 0, 0

        for i, pi in enumerate(pattern):
            if pi == 0:
                continue

            summed_a += ab[i][0]
            summed_b += ab[i][1]

        candidate = summed_a - d * max(0, summed_b - k)
        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
