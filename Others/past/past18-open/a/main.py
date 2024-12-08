# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z, s = map(int, input().split())
    size_max = max(x, y, z)

    if size_max >= s:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
