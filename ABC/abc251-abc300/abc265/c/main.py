# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict, deque
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    g = [list(input().rstrip()) for _ in range(h)]
    sx, sy = 0, 0
    used = defaultdict(int)
    d = deque()
    d.append((sx, sy))

    while d:
        i, j = d.popleft()

        if (i, j) in used:
            print(-1)
            exit()
        
        dir = g[i][j]
        used[(i, j)] += 1

        if dir == "U" and i != 0:
            d.append((i - 1, j))
        elif dir == "D" and i != h - 1:
            d.append((i + 1, j))
        elif dir == "L" and j != 0:
            d.append((i, j - 1))
        elif dir == "R" and j != w - 1:
            d.append((i, j + 1))
        else:
            print(i + 1, j + 1)
            exit()
        


if __name__ == "__main__":
    main()
