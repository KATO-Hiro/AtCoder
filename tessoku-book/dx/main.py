# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque()

    for i, si in enumerate(s, 1):
        if si == "(":
            d.append(i)
        else:
            di = d.pop()
            print(di, i)
    

if __name__ == "__main__":
    main()
