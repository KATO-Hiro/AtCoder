# -*- coding: utf-8 -*-


def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split())) + [x]
    ys = list(map(int, input().split())) + [y]

    x_max = max(xs)
    y_min = min(ys)

    if x_max < y_min:
        print('No War')
    else:
        print('War')


if __name__ == '__main__':
    main()
