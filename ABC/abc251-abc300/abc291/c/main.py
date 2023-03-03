# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    x, y = 0, 0
    dir = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
    d = defaultdict(int)
    d[(0, 0)] = 1

    for si in s:
        dx, dy = dir[si]
        x += dx
        y += dy

        if d[(x, y)] >= 1:
            print("Yes")
            exit()

        d[(x, y)] += 1 

    print("No")
    

if __name__ == "__main__":
    main()
