# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x, l, r = map(int, input().split())

    if l <= x <= r:
        print(x)
    elif x < l:
        print(l)
    else:
        print(r)


if __name__ == '__main__':
    main()
