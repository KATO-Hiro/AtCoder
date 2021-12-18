# -*- coding: utf-8 -*-


def main():
    from bisect import bisect_right
    from itertools import combinations
    import sys

    input = sys.stdin.readline

    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0

    for ki in range(k + 1):
        group1 = list()
        group2 = list()

        for pattern1 in combinations(range(n // 2), ki):
            summed1 = 0

            for p1 in pattern1:
                summed1 += a[p1]
            
            group1.append(summed1)
        
        for pattern2 in combinations(range(n // 2, n), k - ki):
            summed2 = 0

            for p2 in pattern2:
                summed2 += a[p2]
            
            group2.append(summed2)

        group2 = sorted(group2)

        for g1 in group1:
            ans += bisect_right(group2, p - g1)

    print(ans)


if __name__ == "__main__":
    main()
