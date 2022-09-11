# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)

    if n > m:
        print("No")
        exit()

    for si, ti in zip(s, t):
        if si != ti:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
