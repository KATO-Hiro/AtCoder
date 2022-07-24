# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    cd = [tuple(map(int, input().split())) for _ in range(k)]
    ans = 0

    for i, pattern in enumerate(product([0, 1], repeat=k)):
        balls = defaultdict(int)

        for j, pi in enumerate(pattern):
            id = cd[j][pi]
            balls[id] += 1
        
        count = 0

        for ai, bi in ab:
            if balls[ai] > 0 and balls[bi] > 0:
                count += 1
        
        ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
