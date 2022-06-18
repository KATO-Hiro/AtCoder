# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = deque()
    p = 0

    for ai in a:
        d.append(0)

        for i in range(len(d)):
            di = d.popleft()

            if di + ai < 4:
                d.append(di + ai)
            else:
                p += 1
        
    print(p)


if __name__ == "__main__":
    main()
