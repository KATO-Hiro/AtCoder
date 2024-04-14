# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip().lower()

    if t[-1] == "x":
        t = t[:-1]

    m = len(t)

    pos = 0

    for si in s:
        if pos < m and si == t[pos]:
            pos += 1

    if pos == m:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
