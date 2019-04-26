# -*- coding: utf-8 -*-


def main():
    n, va, vb, l = map(int, input().split())

    for i in range(n):
        mod_l = l * vb / va
        l = mod_l

    print('{:.12f}'.format(mod_l))


if __name__ == '__main__':
    main()
