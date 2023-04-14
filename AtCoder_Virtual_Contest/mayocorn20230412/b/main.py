# -*- coding: utf-8 -*-


def main():
    from itertools import permutations
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(n)]
    patterns = permutations(range(1, n))
    costs = list()

    for pattern in patterns:
        pattern = [0] + list(pattern) + [0]
        cost = 0

        for p1, p2 in zip(pattern, pattern[1:]):
            cost += t[p1][p2]
        
        costs.append(cost)
    
    ans = costs.count(k)
    print(ans)


if __name__ == "__main__":
    main()
