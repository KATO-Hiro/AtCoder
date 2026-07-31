# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    for ai in a:
        if ai >= 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
