# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()[::-1]
    ans = deque()
    ans.append(n)

    for i in range(n):
        if s[i] == "L":
            ans.append(n - i - 1)
        else:
            ans.appendleft(n - i - 1)
    
    print(*ans)


if __name__ == "__main__":
    main()
