# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n % 2 == 0:
        m = n // 2 - 1
        bar = "-" * m
        print(bar + "==" + bar)
    else:
        m = n // 2
        bar = "-" * m
        print(bar + "=" + bar)


if __name__ == "__main__":
    main()
