# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    t = input().rstrip()
    a = input().rstrip()

    for ti, ai in zip(t, a):
        if ti == ai == "o":
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
