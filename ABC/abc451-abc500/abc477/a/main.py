# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = "BYRBYR"
    b = input().rstrip()
    index = s.index(b)
    print(s[index + 1])


if __name__ == "__main__":
    main()
