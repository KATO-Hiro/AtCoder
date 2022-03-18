# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    total = sum(a)
    diff = n - total

    if diff >= 0:
        print(diff)
    else:
        print(-1)


if __name__ == "__main__":
    main()
