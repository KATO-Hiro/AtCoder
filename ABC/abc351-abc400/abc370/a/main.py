# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    l, r = map(int, input().split())

    if l == 1 and r == 0:
        pass
        print("Yes")
    elif l == 0 and r == 1:
        print("No")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
