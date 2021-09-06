# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = [0] * (10 ** 5 * 24 + 10)

    for i in range(n):
        di, si, ti = map(int, input().split())
        si_hour = (di - 1) * 24 + si
        t[si_hour] += 1
        ti_hour = (di - 1) * 24 + ti
        t[ti_hour] -= 1
    
    u = list(accumulate(t))

    for ui in u:
        if ui > 1:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
