# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = sorted(input().rstrip())
    print("".join(s))


if __name__ == "__main__":
    main()
