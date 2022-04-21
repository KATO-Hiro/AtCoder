# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    e = sum(a) + sum(b) * 2
    e /= 3
    print(e)


if __name__ == "__main__":
    main()
