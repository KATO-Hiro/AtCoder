# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()[::-1]
    ans = deque()
    ans.append(n)

    for i, si in enumerate(s, 1):
        j = n - i

        if si == "R":
            ans.appendleft(j)
        else:
            ans.append(j)

    print(*ans)


if __name__ == "__main__":
    main()
