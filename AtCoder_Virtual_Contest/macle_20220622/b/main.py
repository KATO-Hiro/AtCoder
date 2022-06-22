# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n = int(input())
    initials = ["M", "A", "R", "C", "H"]
    d = defaultdict(int)
    ans = 0

    for i in range(n):
        s = input().rstrip()
        d[s[0]] += 1

    for pattern in combinations(initials, 3):
        candidate = 1

        for p in pattern:
            candidate *= d[p]
        
        ans += candidate

    print(ans)


if __name__ == "__main__":
    main()
