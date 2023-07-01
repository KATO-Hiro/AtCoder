# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = list(map(int, input().split()))
    t = sorted(s)

    if s != t:
        print("No")
        exit()

    if s == sorted(s) and all(100 <= si <= 675 and si % 25 == 0 for si in s):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
