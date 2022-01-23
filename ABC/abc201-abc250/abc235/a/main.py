# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = input().rstrip()
    a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
    d = a + b + c

    print(111 * d)


if __name__ == "__main__":
    main()
