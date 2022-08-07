# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    red, blue = "r", "b"
    d = deque()
    d.append((red, n, 1))
    ans = 0

    while d:
        color, level, count = d.popleft()
        next_level = level - 1

        if color == red:
            if next_level >= 2:
                d.append((red, next_level, count))
            if level >= 2:
                d.append((blue, level, count * x))
        else:
            if next_level >= 2:
                d.append((red, next_level, count))
                d.append((blue, next_level, count * y))
            elif next_level == 1:
                ans += count * y

    print(ans)


if __name__ == "__main__":
    main()
