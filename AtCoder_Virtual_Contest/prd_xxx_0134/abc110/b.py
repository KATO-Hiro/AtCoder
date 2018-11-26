# -*- coding: utf-8 -*-


def main():
    n, m, x, y = map(int, input().split())
    xs = list(map(int, input().split())) + [x]
    ys = list(map(int, input().split())) + [y]

    if max(xs) < min(ys):
        print('No War')
    else:
        print('War')


if __name__ == '__main__':
    main()
