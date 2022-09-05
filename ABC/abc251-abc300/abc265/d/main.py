# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p, q, r = map(int, input().split())
    a = list(map(int, input().split()))
    y, z, w = 0, 0, 0
    sum_1, sum_2, sum_3 = 0, 0, 0

    for x in range(n):
        while y < n and sum_1 < p:
            sum_1 += a[y]
            sum_2 -= a[y]
            y += 1

        while z < n and sum_2 < q:
            sum_2 += a[z]
            sum_3 -= a[z]
            z += 1

        while w < n and sum_3 < r:
            sum_3 += a[w]
            w += 1

        if sum_1 == p and sum_2 == q and sum_3 == r:
            print("Yes")
            exit()
        
        sum_1 -= a[x]
    
    print("No")


if __name__ == "__main__":
    main()