# -*- coding: utf-8 -*-


def main():
    from statistics import median
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for i in range(1, n + 1):
        a[i - 1] -= i
    
    ans = 0
    med_a = median(a)

    for ai in a:
        ans += abs(ai - med_a)
    
    print(int(ans))


if __name__ == "__main__":
    main()
