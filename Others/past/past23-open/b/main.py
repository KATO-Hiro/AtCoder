# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())

    if a + c == b:
        x, y = a, b
    elif b + c == a:
        x, y = b, a

    if c > 0:
        c = "+" + str(c)

    print(f"{x} -> {y} ({c})")


if __name__ == "__main__":
    main()
