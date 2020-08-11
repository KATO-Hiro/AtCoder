# -*- coding: utf-8 -*-


def main():
    from decimal import Decimal
    import sys
    input = sys.stdin.readline

    a, b = input().split()
    a = int(a)
    b = Decimal(b)
    b *= 100
    ans = int((a * b) / 100)
    print(ans)


if __name__ == '__main__':
    main()
