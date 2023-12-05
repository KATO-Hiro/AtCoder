# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    c = a + b

    print(len(list(str(c))))


if __name__ == "__main__":
    main()
