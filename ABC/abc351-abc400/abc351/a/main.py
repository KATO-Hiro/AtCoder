# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(sum(a) - sum(b) + 1)


if __name__ == "__main__":
    main()
