# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    a, b = input().split()
    a = int(a, k)
    b = int(b, k)
    print(a * b)


if __name__ == "__main__":
    main()
