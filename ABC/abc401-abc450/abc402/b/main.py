# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    q = int(input())
    d = deque()

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            d.append(query[1])
        else:
            di = d.popleft()
            print(di)


if __name__ == "__main__":
    main()
