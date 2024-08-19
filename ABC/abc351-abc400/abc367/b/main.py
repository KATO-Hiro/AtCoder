# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x = input().rstrip()

    while x[-1] == "0":
        x = x[:-1]

        if x[-1] == ".":
            break

    if x[-1] == ".":
        x = x[:-1]

    print(x)


if __name__ == "__main__":
    main()
