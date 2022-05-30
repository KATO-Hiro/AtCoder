# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    r, c = map(int, input().split())
    dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    ans = 0

    for dx, dy in dxy:
        x = c + dx
        y = r + dy

        if 1 <= x <= w and 1 <= y <= h:
            ans += 1
    
    print(ans)


if __name__ == "__main__":
    main()
