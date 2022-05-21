# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase
    import sys

    input = sys.stdin.readline

    n = int(input())
    n -= 97
    print(ascii_lowercase[n])


if __name__ == "__main__":
    main()
