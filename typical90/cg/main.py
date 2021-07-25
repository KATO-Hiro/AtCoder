# -*- coding: utf-8 -*-


def main():
    from math import sqrt
    import sys

    input = sys.stdin.readline

    k = int(input())
    p = set()

    for i in range(1, int(sqrt(k)) + 1):
        if k % i == 0:
            p.add(i)
            p.add(k // i)
    
    ans = 0
    
    for a in p:
        for b in p:
            c, q = divmod(k, a * b)
            if q == 0 and (a <= b <= c):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
