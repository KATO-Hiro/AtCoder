# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))
    acc = list(accumulate([0] + a))
    ans = 0

    for i in range(1, n):
        ans += a[i] * i - acc[i]
    
    print(ans)


if __name__ == "__main__":
    main()
