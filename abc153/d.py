# -*- coding: utf-8 -*-

def rec(x):
    if x == 1:
        return 1

    return 2 * rec(x // 2) + 1


def main():
    from sys import setrecursionlimit

    setrecursionlimit(10 ** 7)

    n = int(input())
    print(rec(n))


if __name__ == '__main__':
    main()
