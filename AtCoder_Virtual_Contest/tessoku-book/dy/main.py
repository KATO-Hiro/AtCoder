# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n, x = map(int, input().split())
    a = list(input().rstrip())
    a[x - 1] = "@"
    q = deque([x - 1])

    while q:
        pos = q.popleft()

        if pos - 1 >= 0 and a[pos - 1] == ".":
            a[pos - 1] = "@"
            q.append(pos - 1)
        if pos + 1 < n and a[pos + 1] == ".":
            a[pos + 1] = "@"
            q.append(pos + 1)

    print("".join(a))


if __name__ == "__main__":
    main()
