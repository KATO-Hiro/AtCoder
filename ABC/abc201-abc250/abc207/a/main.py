# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = sorted(list(map(int, input().split())))
    print(sum(abc[1:]))


if __name__ == "__main__":
    main()
