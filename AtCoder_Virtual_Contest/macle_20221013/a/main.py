# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    s, t = map(str, input().split())
    a, b = map(int, input().split())
    u = input().rstrip()

    if u == s:
        a -= 1
    else:
        b -= 1

    print(a, b)


if __name__ == "__main__":
    main()
