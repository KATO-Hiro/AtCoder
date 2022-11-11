# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = input().rstrip()

    if len(set(list(n))) == 1:
        print("Yes")
    elif len(set(list(n[:3]))) == 1 or len(set(list(n[1:]))) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
