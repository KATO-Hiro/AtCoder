# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = "".join(input().rstrip().replace(" ", "")[::-1])
    print(int(a, 2))


if __name__ == "__main__":
    main()
