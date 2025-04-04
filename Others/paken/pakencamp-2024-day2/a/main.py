# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    print(a[3] - a[4])


if __name__ == "__main__":
    main()
