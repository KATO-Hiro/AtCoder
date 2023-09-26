# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = int(s)
    m = 0

    for si in s:
        m += int(si)

    if n % m == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
