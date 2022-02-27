# -*- coding: utf-8 -*-


def main():
    from decimal import Decimal
    import sys

    input = sys.stdin.readline

    x = input()
    y, z = divmod(Decimal(x), 10)

    if int(x) < 0 and int(z) != 0:
        y -= 1
    
    print(y)


if __name__ == "__main__":
    main()
