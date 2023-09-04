# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().split("/")

    if int(s[1]) <= 4:
        print("Heisei")
    else:
        print("TBD")


if __name__ == "__main__":
    main()
