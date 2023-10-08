# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()

    for i, si in enumerate(s, 1):
        if i % 2 == 0 and si != "0":
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
