# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        ai, bi = map(int, input().split())

        if ai > bi:
            print("Left")
        elif ai == bi:
            print("Balanced")
        else:
            print("Right")


if __name__ == "__main__":
    main()
