# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    u = set()
    u.add("dream"[::-1])
    u.add("dreamer"[::-1])
    u.add("erase"[::-1])
    u.add("eraser"[::-1])

    s = input().rstrip()[::-1]
    d = deque(s)

    while d:
        tmp = ""

        for i in range(7):
            di = d.popleft()
            tmp += di

            if tmp in u:
                break

            if i == 6:
                print("NO")
                exit()

    print("YES")


if __name__ == "__main__":
    main()
