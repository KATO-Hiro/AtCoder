# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    cost = n * 108 // 100

    if cost < 206:
        print("Yay!")
    elif cost == 206:
        print("so-so")
    else:
        print(":(")


if __name__ == "__main__":
    main()
