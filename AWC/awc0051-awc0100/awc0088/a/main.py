# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    t = list(map(int, input().split()))
    print(max(t) + k)


if __name__ == "__main__":
    main()
