# -*- coding: utf-8 -*-


def main():
    from itertools import product
    import sys

    input = sys.stdin.readline

    n, m, x = map(int, input().split())
    patterns = product([0, 1], repeat=n)
    books = [list(map(int, input().split())) for _ in range(n)]
    ans = float('inf')

    for pattern in patterns:
        values = [0] * m
        costs = 0
        ok = True

        for i, pi in enumerate(pattern):
            if pi == 0:
                continue

            cost, book = books[i][0], books[i][1:]
            costs += cost

            for j, bi in enumerate(book):
                values[j] += bi
        
        for value in values:
            if value < x:
                ok = False
        
        if ok:
            ans = min(ans, costs)
    
    if ans == float("inf"):
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
