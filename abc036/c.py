# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    compressed_a = sorted(set(a))
    d = dict()

    for key, value in enumerate(compressed_a):
        d[value] = key

    for ai in a:
        print(d[ai])


if __name__ == '__main__':
    main()
