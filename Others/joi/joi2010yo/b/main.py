# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = [int(input()) for _ in range(n)] + [0 for _ in range(10 ** 5)]
    b = [int(input()) for _ in range(m)]
    pos = 0

    for index, bi in enumerate(b):
        pos += bi
        pos += a[pos]

        if pos >= n - 1:
            print(index + 1)
            exit()


if __name__ == '__main__':
    main()
