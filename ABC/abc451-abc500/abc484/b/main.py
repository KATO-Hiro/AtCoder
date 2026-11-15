# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    k = int(input())
    a = list(map(int, input().split()))

    if 9 not in a:
        print(-1)
    else:
        print(min(a))


if __name__ == "__main__":
    main()
