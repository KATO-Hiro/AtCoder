# -*- coding: utf-8 -*-


def main():
    n, b1, b2, b3 = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    r = [list(map(int, input().split())) for _ in range(n)]

    for ri in r:
        print(' '.join(map(str, ri)))


if __name__ == '__main__':
    main()
