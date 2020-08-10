# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate

    n = int(input())
    brightness = [0] * (10 ** 6 + 2)

    for i in range(n):
        a, b = map(int, input().split())
        brightness[a] += 1
        brightness[b + 1] -= 1

    print(max(accumulate(brightness)))


if __name__ == '__main__':
    main()
