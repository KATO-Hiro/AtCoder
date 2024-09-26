# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    print(s.replace(".", ""))


if __name__ == "__main__":
    main()
