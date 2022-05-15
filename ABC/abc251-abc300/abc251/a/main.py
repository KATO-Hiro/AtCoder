# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    ans = s * (6 // n)
    print(ans)


if __name__ == "__main__":
    main()
