# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p = set()

    for i in range(1, int(sqrt(m))):
        if m % i == 0:
            p.add(i)
            p.add(m // i)
    
    ans = 1

    for pi in p:
        if m // pi >= n:
            ans = max(ans, pi)

    print(ans)


if __name__ == "__main__":
    main()
