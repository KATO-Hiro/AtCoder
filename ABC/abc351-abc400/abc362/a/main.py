# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    r, g, b = map(int, input().split())
    c = input().rstrip()

    if c == "Red":
        print(min(g, b))
    elif c == "Green":
        print(min(r, b))
    else:
        print(min(r, g))


if __name__ == "__main__":
    main()
