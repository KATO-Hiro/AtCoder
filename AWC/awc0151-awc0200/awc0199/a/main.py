# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    ans = (a // c) * (b // c)
    print(ans)


if __name__ == "__main__":
    main()
