# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    abc = sorted([int(input()) for _ in range(3)])

    if abc[0] + abc[1] == abc[2]:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    main()
