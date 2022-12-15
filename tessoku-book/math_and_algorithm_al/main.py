# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    t = int(input())
    n = int(input())
    imos = [0] * (5 * 10 ** 5 + 10)

    for _ in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1
    
    imos = list(accumulate(imos))
    
    for i in range(t):
        print(imos[i])


if __name__ == "__main__":
    main()
