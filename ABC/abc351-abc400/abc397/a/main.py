# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip().replace(".", "")
    n = int(s)

    if n >= 380:
        print(1)
    elif 375 <= n < 380:
        print(2)
    else:
        print(3)


if __name__ == "__main__":
    main()
