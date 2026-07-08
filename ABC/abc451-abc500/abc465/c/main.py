# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    rev_count = 0
    d = deque()

    for i, si in enumerate(s, 1):
        if si == "o":
            rev_count += 1

            if rev_count % 2 == 0:
                d.append(i)
            else:
                d.appendleft(i)
        else:
            if rev_count % 2 == 0:
                d.appendleft(i)
            else:
                d.append(i)

    if rev_count % 2 == 0:
        d = list(d)[::-1]

    print(*d)


if __name__ == "__main__":
    main()
