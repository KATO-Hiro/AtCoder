# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import accumulate

    input = sys.stdin.readline

    d = int(input())
    n = int(input())
    imos = [0] * (d + 10)

    for _ in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri + 1] -= 1

    imos = list(accumulate(imos))

    for i in range(1, d + 1):
        print(imos[i])


if __name__ == "__main__":
    main()
