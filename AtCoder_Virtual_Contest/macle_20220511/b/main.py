# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    conds = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    actions = [tuple(map(int, input().split())) for _ in range(k)]
    ans = 0
    
    for balls in product(*actions):
        balls = set(balls)
        count = 0
        
        for ai, bi in conds:
            if ai in balls and bi in balls:
                count += 1

        ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
