# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b = map(int, input().split())

    if a == 1 and b == 2:
        print("Yes")
    elif a == 2 and b == 3:
        print("Yes")
    elif a == 4 and b == 5:
        print("Yes")
    elif a == 5 and b == 6:
        print("Yes")
    elif a == 7 and b == 8:
        print("Yes")
    elif a == 8 and b == 9:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
