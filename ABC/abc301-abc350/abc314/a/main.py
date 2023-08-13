# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    print(s[: n + 2])


if __name__ == "__main__":
    main()
