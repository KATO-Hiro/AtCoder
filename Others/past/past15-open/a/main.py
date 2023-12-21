# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, t = map(int, input().split())
    print(5 * a + t)


if __name__ == "__main__":
    main()
