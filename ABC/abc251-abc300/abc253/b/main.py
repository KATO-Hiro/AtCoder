# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [input().rstrip() for _ in range(h)]
    points = list()

    for i in range(h):
        for j in range(w):
            if s[i][j] == 'o':
                points.append((i, j))

    x = abs(points[0][0] - points[1][0])
    y = abs(points[0][1] - points[1][1])
    
    print(x + y)


if __name__ == "__main__":
    main()
