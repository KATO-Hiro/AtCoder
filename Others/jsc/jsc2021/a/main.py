# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())

    for ans in range(10 ** 6 + 1, -1, -1):
        if ans * x < y * z:
            print(ans)
            exit()


if __name__ == "__main__":
    main()
