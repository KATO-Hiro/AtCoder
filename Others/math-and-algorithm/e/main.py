# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    print(sum(a) % 100)


if __name__ == "__main__":
    main()
