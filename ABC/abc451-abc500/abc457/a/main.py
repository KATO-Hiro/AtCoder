# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    x -= 1
    print(a[x])


if __name__ == "__main__":
    main()
