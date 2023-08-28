# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = set(map(int, input().split()))
    print(len(abc))


if __name__ == "__main__":
    main()
