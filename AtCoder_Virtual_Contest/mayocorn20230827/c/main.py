# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = int(input())
    upper = 200

    for a in range(-upper, upper + 1):
        for b in range(-upper, upper + 1):
            if (a**5) - (b**5) == x:
                print(a, b)
                exit()


if __name__ == "__main__":
    main()
