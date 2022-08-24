# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    t = [int(input()) for _ in range(5)]
    ans = float("inf")

    for pattern in permutations(t):
        cost = 0

        for i, pi in enumerate(pattern, 1):
            if i == 5:
                cost += pi
                continue

            p, q = divmod(pi, 10)
            cost += p * 10

            if q != 0:
                cost += 10
        
        ans = min(ans, cost)

    print(ans)


if __name__ == "__main__":
    main()
