# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = int(input())

    if 200 <= s < 300:
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()
