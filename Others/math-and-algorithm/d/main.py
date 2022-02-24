# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a1, a2, a3  = map(int, input().split())
    print(a1 * a2 * a3)


if __name__ == "__main__":
    main()
