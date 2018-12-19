# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    colors = [0] * (10 ** 6 + 2)

    for i in range(n):
        ai, bi = map(int, input().split())
        colors[ai] += 1
        colors[bi + 1] += -1

    print(max(list(accumulate(colors))))


if __name__ == '__main__':
    main()
