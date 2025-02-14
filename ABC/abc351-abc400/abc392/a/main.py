# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = sorted(list(map(int, input().split())))

    if a[0] * a[1] == a[2]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
