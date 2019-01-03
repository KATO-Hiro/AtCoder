# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    cost = float('inf')

    for i in range(-100, 100 + 1):
        total = 0

        for ai in a:
            total += (ai - i) ** 2

        cost = min(cost, total)

    print(cost)


if __name__ == '__main__':
    main()
