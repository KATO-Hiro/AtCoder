# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    s = input().rstrip()
    d = deque()
    ans = list()

    for i, si in enumerate(s, 1):
        if si == "(":
            d.append(i)
        else:
            left = d.pop()
            ans.append((left, i))

    for left, right in ans:
        print(left, right)


if __name__ == "__main__":
    main()
