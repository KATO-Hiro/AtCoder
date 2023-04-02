# -*- coding: utf-8 -*-


def main():
    from math import ceil, sqrt
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    inf = float("inf")
    ans = inf

    for a in range(1, ceil(sqrt(m)) + 1):
        b = ceil(m / a)

        if a <= n and b <= n:
            ans = min(ans, a * b)
    
    if ans == inf:
        ans = -1

    print(ans)
    

if __name__ == "__main__":
    main()
