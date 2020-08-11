# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    a = [0] * m
    item_count = 0
    cost = 0

    for i in range(m):
        ai, bi = map(int, input().split())
        a[i] = ai

    for ai in sorted(a, reverse=True):
        if item_count >= m - 1:
            print(cost)
            exit()

        if ai < n:
            cost += n - ai

        item_count += 1


if __name__ == '__main__':
    main()
