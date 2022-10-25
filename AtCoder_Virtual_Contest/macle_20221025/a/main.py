# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = input().rstrip().split("x")
    print(int(a) * int(b))


if __name__ == "__main__":
    main()
