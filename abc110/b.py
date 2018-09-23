# -*- coding: utf-8 -*-


def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split()))
    ys = list(map(int, input().split()))

    x_max = max(xs) + 1
    y_min = min(ys)

    if x_max > y_min:
        print('War')
        exit()

    if x_max == y_min:
        if x < x_max <= y:
            print('No War')
            exit()

    for z in range(x_max, y_min + 1):
        if x < z <= y:
            print('No War')
            exit()

    print('War')


if __name__ == '__main__':
    main()
