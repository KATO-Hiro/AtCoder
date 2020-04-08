# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    s, l, r = map(int, input().split())

    if s < l:
        print(l)
    elif s > r:
        print(r)
    else:
        print(s)


if __name__ == '__main__':
    main()
