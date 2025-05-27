# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    x, y = map(int, input().split())
    p = set()

    for i in range(1, 7):
        for j in range(1, 7):
            if (i + j >= x) or abs(i - j) >= y:
                p.add((i, j))

    ans = len(p) / 36
    print(ans)


if __name__ == "__main__":
    main()
