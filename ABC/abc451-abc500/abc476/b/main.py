# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()

    for si, ti in zip(s, t):
        if ti == "*":
            continue
        if si == ti:
            continue

        print("No")
        exit()

    print("Yes")


if __name__ == "__main__":
    main()
