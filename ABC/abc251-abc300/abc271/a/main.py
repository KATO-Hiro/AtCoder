# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = hex(n)[2:].zfill(2).upper()
    print(ans)


if __name__ == "__main__":
    main()
