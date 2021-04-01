# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = int(input())

    for i in range(t):
        case = int(input())

        if case % 4 == 0:
            print("Even")
        elif case % 4 == 2:
            print("Same")
        else:
            print("Odd")


if __name__ == "__main__":
    main()
