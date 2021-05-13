# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)

    for i in range(n // 4):
        if s[4 * i : 4 * i + 4] == "post":
            print(i + 1)
            exit()

    print("none")


if __name__ == "__main__":
    main()
