# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    conds = list()

    for i in range(m):
        ai, bi = map(int, input().split())
        ai, bi = ai - 1, bi - 1
        conds.append((ai, bi))
    
    k = int(input())
    balls = list()

    for i in range(k):
        ci, di = map(int, input().split())
        ci, di = ci - 1, di - 1
        balls.append((ci, di))

    ans = 0
    
    for pattern in product([0, 1], repeat=k):
        dishes = [0] * n
        
        for i, p in enumerate(pattern):
            ci, di = balls[i]

            if p == 0:
                dishes[ci] += 1
            else:
                dishes[di] += 1
        
        count = 0
        
        for i, (ai, bi) in enumerate(conds):
            if dishes[ai] >= 1 and dishes[bi] >= 1:
                count += 1

        ans = max(ans, count)
    
    print(ans)


if __name__ == "__main__":
    main()
