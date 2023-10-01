# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = sorted(set(map(int, input().split())))

    for ai in a:
        print(ai)


if __name__ == "__main__":
    main()
