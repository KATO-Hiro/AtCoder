# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    summed = sum(a)

    for ai in a:
        if summed - ai == m:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
