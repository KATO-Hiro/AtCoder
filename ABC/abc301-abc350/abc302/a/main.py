# -*- coding: utf-8 -*-


def ceil(a: int, b: int) -> int:
    assert b != 0

    return (a + b - 1) // b


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())
    print(ceil(a, b))


if __name__ == "__main__":
    main()
