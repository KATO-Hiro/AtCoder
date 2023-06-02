# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    for i in range(a, b + 1):
        if 100 % i == 0:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
