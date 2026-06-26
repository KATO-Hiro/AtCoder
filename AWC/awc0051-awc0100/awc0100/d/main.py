# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    summed = sum(a)
    acc = list(accumulate(a, initial=0))
    inf = 10**18
    ans = inf

    for i in range(1, n):
        s1 = acc[i]
        s2 = summed - s1
        ans = min(ans, abs(s1 - s2))

    print(ans)


if __name__ == "__main__":
    main()
