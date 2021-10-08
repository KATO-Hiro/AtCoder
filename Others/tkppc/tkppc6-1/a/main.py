# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n >= 2018:
        print(n - 2015)
    elif n == 2015 or n == 2016:
        print(n - 2014)
    else:
        print(-1)


if __name__ == "__main__":
    main()
