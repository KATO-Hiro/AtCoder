# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, l, r = map(int, input().split())
    s = input().rstrip()
    l -= 1

    for i in range(l, r):
        if s[i] == "x":
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
