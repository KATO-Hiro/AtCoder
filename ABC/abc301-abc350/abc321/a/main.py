# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    if len(s) == 1:
        print("Yes")
        exit()

    for i, j in zip(s, s[1:]):
        if int(i) <= int(j):
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
