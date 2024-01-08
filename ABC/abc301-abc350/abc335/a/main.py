# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(input().rstrip())
    s[-1] = "4"
    print("".join(s))


if __name__ == "__main__":
    main()
