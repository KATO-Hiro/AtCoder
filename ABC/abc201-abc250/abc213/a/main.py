# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    for c in range(255 + 1):
        if a ^ c == b:
            print(c)
            exit()


if __name__ == "__main__":
    main()
