# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    t = input().rstrip()
    n, m = len(s), len(t)

    if n <= m and t.startswith(s):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
