# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, t, a = map(int, input().split())
    n += 1

    if t * 2 >= n or a * 2 >= n:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
