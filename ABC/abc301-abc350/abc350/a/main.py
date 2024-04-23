# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    number = int(s[3:])

    if (1 <= number <= 315) or (317 <= number <= 349):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
