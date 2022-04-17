# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = set(input().rstrip())
    numbers = set([str(i) for i in range(10)])
    print(*list(s ^ numbers))


if __name__ == "__main__":
    main()
