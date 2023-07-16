# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, p, q = map(int, input().split())
    d = list(map(int, input().split()))
    print(min(p, q + min(d)))


if __name__ == "__main__":
    main()
