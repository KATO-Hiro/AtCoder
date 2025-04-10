# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    t = input().rstrip()
    count = 0

    for si, ti in zip(s, t):
        if si != ti:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
