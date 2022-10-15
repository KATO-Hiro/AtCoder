# -*- coding: utf-8 -*-


def main():
    from math import factorial
    import sys

    input = sys.stdin.readline

    n = int(input())
    print(factorial(n))


if __name__ == "__main__":
    main()
