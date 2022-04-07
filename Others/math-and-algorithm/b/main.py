# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    print(sum(a))


if __name__ == "__main__":
    main()
