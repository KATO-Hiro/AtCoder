# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    w, h, x, y = map(int, input().split())
    s = (w * h) / 2
    count = 0

    if x * 2 == w and y * 2 == h:
        count = 1
    
    print(s, count)


if __name__ == "__main__":
    main()
