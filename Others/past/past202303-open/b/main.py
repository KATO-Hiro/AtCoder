# -*- coding: utf-8 -*-


def main():
    import sys
    from decimal import Decimal, getcontext

    input = sys.stdin.readline

    # See:
    # https://docs.python.org/ja/3/library/decimal.html
    getcontext().prec = 1000

    d = int(input())

    a = Decimal(input())
    b = Decimal(input())
    print(a + b)


if __name__ == "__main__":
    main()
