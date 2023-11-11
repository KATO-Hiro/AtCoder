# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque()

    for si in s:
        if si == "C":
            if len(d) >= 2 and d[-1] == "B" and d[-2] == "A":
                d.pop()
                d.pop()
            else:
                d.append(si)
        else:
            d.append(si)

    print("".join(d))


if __name__ == "__main__":
    main()
