# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    t = int(input())
    n = int(input())
    imos = [0] * (t + 1)

    for i in range(n):
        li, ri = map(int, input().split())
        imos[li] += 1
        imos[ri] -= 1
    
    print('\n'.join(map(str, list(accumulate(imos[:-1])))))


if __name__ == "__main__":
    main()
