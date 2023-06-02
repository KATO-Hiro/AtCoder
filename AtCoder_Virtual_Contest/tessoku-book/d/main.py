# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    print(bin(n)[2:].zfill(10))


if __name__ == "__main__":
    main()
