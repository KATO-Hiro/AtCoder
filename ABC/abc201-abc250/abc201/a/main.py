# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = sorted(list(map(int, input().split())), reverse=True)

    if a[2] - a[1] == a[1] - a[0]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
