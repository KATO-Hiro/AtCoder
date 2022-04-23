# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    q = int(input())
    d = deque()

    for i in range(q):
        qi = list(map(int, input().split()))

        if qi[0] == 1:
            x, c = qi[1], qi[2]
            d.append((x, c))
        else:
            c = qi[1]
            summed = 0

            while c > 0:
                xi, ci = d.popleft()

                if c <= ci:
                    summed += xi * c
                    print(summed)

                    if c != ci:
                        d.appendleft((xi, ci - c))

                    c = 0
                else:
                    summed += xi * ci
                    c -= ci


if __name__ == "__main__":
    main()
