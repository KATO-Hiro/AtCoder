# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())
    l -= 1
    s = input().rstrip()

    print(s[:l] + s[l:r][::-1] + s[r:])


if __name__ == "__main__":
    main()
