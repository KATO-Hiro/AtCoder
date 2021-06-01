# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(reversed(input().rstrip()))

    for index, si in enumerate(s):
        if si == "6":
            s[index] = "9"
        elif si == "9":
            s[index] = "6"

    print("".join(map(str, s)))


if __name__ == "__main__":
    main()
