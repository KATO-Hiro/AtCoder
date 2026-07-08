# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    rev = False
    d = deque()

    for i, si in enumerate(s, 1):
        if rev:
            d.appendleft(i)
        else:
            d.append(i)

        rev ^= si == "o"

    if rev:
        d = list(d)[::-1]

    print(*d)


if __name__ == "__main__":
    main()
