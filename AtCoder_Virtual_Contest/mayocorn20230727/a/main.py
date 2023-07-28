# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for i in range(n, 1000):
        if i % 111 == 0:
            print(i)
            exit()


if __name__ == "__main__":
    main()
