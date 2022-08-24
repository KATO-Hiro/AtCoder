# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = float("inf")

    for pattern in product([0, 1], repeat=n):
        if sum(pattern) == 0:
            continue

        candidate = 0
        tmp = 0

        for i, pi in enumerate(pattern):
            tmp |= a[i]

            if pi == 1:
                candidate ^= tmp
                tmp = 0
        
        if tmp != 0:
            candidate ^= tmp

        ans = min(ans, candidate)
    
    print(ans)


if __name__ == "__main__":
    main()
