# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x1, y1, x2, y2 = map(int, input().split())
    dxy = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]

    for dx, dy in dxy:
        x = x1 + dx
        y = y1 + dy

        if (x - x2) ** 2 + (y - y2) ** 2 == 5:
            print("Yes")
            exit()
    
    print("No")


if __name__ == "__main__":
    main()
