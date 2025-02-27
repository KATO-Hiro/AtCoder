# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    counts = s.count("2")
    print("2" * counts)


if __name__ == "__main__":
    main()
