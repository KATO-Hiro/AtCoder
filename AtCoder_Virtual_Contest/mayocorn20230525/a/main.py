# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    h = int(input())
    print((a + b) * h // 2)


if __name__ == "__main__":
    main()
