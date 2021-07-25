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
    sorted_p = sorted(p)
    n = len(p)
    
    for i in range(n):
        for j in range(i, n):
            a = sorted_p[i]
            b = sorted_p[j]
            c, q = divmod(k, a * b)

            if q == 0 and (c >= b):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
