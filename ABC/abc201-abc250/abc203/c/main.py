# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    ab = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        ab.append((ai, bi))

    sorted_ab = sorted(ab)
    money = k

    for pos, value in sorted_ab:
        if money >= pos:
            money += value

    print(money)


if __name__ == "__main__":
    main()
