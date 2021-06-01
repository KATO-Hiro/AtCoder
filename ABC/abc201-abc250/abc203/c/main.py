# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    d = defaultdict()

    for i in range(n):
        ai, bi = map(int, input().split())

        if ai in d.keys():
            d[ai] += bi
        else:
            d[ai] = bi

    sorted_d = sorted(d.items(), key=lambda x: x[0])
    pos = 0
    money = k

    for key, value in sorted_d:
        diff = key - pos

        if diff <= money:
            money -= diff
            pos = key
            money += value
        else:
            pos += money
            print(pos)
            exit()

    print(pos + money)


if __name__ == "__main__":
    main()
