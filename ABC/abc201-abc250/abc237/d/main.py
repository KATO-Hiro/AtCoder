# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    d = deque()
    d.append(n)

    for i in range(n - 1, -1, -1):
        if s[i] == "L":
            d.append(i)
        else:
            d.appendleft(i)
    
    print(*d)


if __name__ == "__main__":
    main()
