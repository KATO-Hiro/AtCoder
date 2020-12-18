# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    plus = a + b
    minus = a - b
    print(max(plus, minus))
    print(min(plus, minus))


if __name__ == "__main__":
    main()
