# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy1 = [tuple(map(int, input().split())) for _ in range(n)]
    m = int(input())
    xy2 = [tuple(map(int, input().split())) for _ in range(m)]
    xy2 = set(xy2)

    for x1, y1 in xy1:
        for x2, y2 in xy2:
            dx, dy = x2 - x1, y2 - y1
            count = 0

            for x3, y3 in xy1:
                nx, ny = x3 + dx, y3 + dy

                if (nx, ny) in xy2:
                    count += 1

            if count == n:
                print(dx, dy)
                exit()


if __name__ == "__main__":
    main()
