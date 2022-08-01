# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, w = map(int, input().split())
    t_max = 2 * 10 ** 5 + 10
    imos = [0] * t_max

    for i in range(n):
        si, ti, pi = map(int, input().split())
        imos[si] += pi
        imos[ti] -= pi
    
    imos = list(accumulate(imos))

    for i in imos:
        if i > w:
            print("No")
            exit()
    
    print("Yes")


if __name__ == "__main__":
    main()
