# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    s = input().rstrip() + "Z"
    t = input().rstrip()

    for i, (si, ti) in enumerate(zip(s, t), 1):
        if si != ti:
            print(i)
            exit()


if __name__ == "__main__":
    main()
