# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = deque()

    for _ in range(q):
        qi = list(map(str, input().split()))

        if qi[0] == "1":
            d.append(qi[1])
        elif qi[0] == "2":
            print(d[0])
        else:
            d.popleft()


if __name__ == "__main__":
    main()
