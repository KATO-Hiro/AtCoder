# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = int(input())
    b = int(input())

    for i in range(1, 4):
        if i == a or i == b:
            continue

        print(i)


if __name__ == "__main__":
    main()
