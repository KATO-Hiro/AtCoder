# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    t = int(input())
    n = int(input())
    imos = [0] * (t + 10)

    for _ in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1

    imos = list(accumulate(imos))

    for i in range(t):
        print(imos[i])


if __name__ == "__main__":
    main()
