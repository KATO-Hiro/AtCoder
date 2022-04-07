# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = set(map(int, input().split()))

    if len(abc) == 2:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
