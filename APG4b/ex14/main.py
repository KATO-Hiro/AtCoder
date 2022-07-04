# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = list(map(int, input().split()))
    print(max(abc) - min(abc))


if __name__ == "__main__":
    main()
