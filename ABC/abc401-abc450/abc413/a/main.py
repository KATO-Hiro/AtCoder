# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    if sum(a) <= m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
