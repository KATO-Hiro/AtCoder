# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    c = set()

    for si, ti in zip(s, t):
        c.add((ord(si) - ord(ti)) % 26)

    if len(c) == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
