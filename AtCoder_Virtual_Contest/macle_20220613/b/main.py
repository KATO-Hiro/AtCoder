# -*- coding: utf-8 -*-


def main():
    from decimal import Decimal
    import sys

    input = sys.stdin.readline

    a, b = map(Decimal, input().split())

    print(int(a * b))


if __name__ == "__main__":
    main()
