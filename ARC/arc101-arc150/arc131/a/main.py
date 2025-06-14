# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())
    b *= 10
    b //= 2

    ans = str(b) + "0" + str(a)
    print(ans)


if __name__ == "__main__":
    main()
