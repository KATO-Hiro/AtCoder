# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    ans = deque()

    while True:
        ai = int(input())
        ans.appendleft(ai)

        if ai == 0:
            break

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
