# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque()

    for si in s:
        if si == "0":
            d.append("0")
        elif si == "1":
            d.append("1")
        else:
            if len(d) > 0:
                d.pop()
    
    print("".join(d))


if __name__ == "__main__":
    main()
