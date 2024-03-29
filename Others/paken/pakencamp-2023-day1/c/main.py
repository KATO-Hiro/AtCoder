# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)

    if a_max >= 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
