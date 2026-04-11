# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import product

    input = sys.stdin.readline

    n = int(input())
    l = list(map(int, input().split()))
    patterns = product([-1, 1], repeat=n)
    ans = 0

    for pattern in patterns:
        prev = 0.5
        candidate = 0

        for pi, li in zip(pattern, l):
            cur = prev + pi * li

            if prev * cur < 0:
                candidate += 1

            prev = cur

        ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
