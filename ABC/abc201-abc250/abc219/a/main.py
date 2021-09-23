# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())

    if x >= 90:
        print("expert")
    elif 70 <= x < 90:
        print(90 - x)
    elif 40 <= x < 70:
        print(70 - x)
    else:
        print(40 - x)


if __name__ == "__main__":
    main()
