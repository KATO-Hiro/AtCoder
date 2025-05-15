# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, x = map(int, input().split())

    if x == 1:
        if 1600 <= r < 3000:
            print("Yes")
        else:
            print("No")
    else:
        if 1200 <= r < 2400:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
