# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    d = deque()
    error = "ERROR"

    for index, si in enumerate(s, 1):
        if si == "L":
            d.appendleft(index)
        elif si == "R":
            d.append(index)
        elif si == "A":
            if len(d) <= 0:
                print(error)
            else:
                print(d.popleft())
        elif si == "B":
            if len(d) <= 1:
                print(error)
            else:
                d1 = d.popleft()
                print(d.popleft())
                d.appendleft(d1)
        elif si == "C":
            if len(d) <= 2:
                print(error)
            else:
                d1 = d.popleft()
                d2 = d.popleft()
                print(d.popleft())
                d.appendleft(d2)
                d.appendleft(d1)
        elif si == "D":
            if len(d) <= 0:
                print(error)
            else:
                print(d.pop())
        elif si == "E":
            if len(d) <= 1:
                print(error)
            else:
                d1 = d.pop()
                print(d.pop())
                d.append(d1)
        elif si == "F":
            if len(d) <= 2:
                print(error)
            else:
                d1 = d.pop()
                d2 = d.pop()
                print(d.pop())
                d.append(d2)
                d.append(d1)


if __name__ == "__main__":
    main()
