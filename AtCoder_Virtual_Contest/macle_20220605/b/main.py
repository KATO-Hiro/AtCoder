# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    a = deque()
    a.append(n)

    for i, si in enumerate(reversed(s)):
        m = n - i - 1

        if si == 'L':
            a.append(m)
        else:
            a.appendleft(m)
    
    print(*a)


if __name__ == "__main__":
    main()
