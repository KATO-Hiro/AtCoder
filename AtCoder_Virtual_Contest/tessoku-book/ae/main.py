# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = n // 3 + n // 5 - n // 15
    print(ans)


if __name__ == "__main__":
    main()
