# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, d = map(int, input().split())

    for i in range(n):
        xi, yi = map(int, input().split())

        if xi < s and yi > d:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
