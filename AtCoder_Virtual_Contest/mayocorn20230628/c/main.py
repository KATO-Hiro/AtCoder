# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, x = map(int, input().split())
    s = input().rstrip()
    x = list(bin(x)[2:])
    d = deque(x)

    for si in s:
        if si == "U":
            d.pop()
        elif si == "L":
            d.append("0")
        else:
            d.append("1")

    print(int("".join(d), 2))


if __name__ == "__main__":
    main()
