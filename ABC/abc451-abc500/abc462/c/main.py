# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    xy = [tuple(map(int, input().split())) for _ in range(n)]
    xy.sort()
    y_min = n + 1
    ans = 0

    for _, yi in xy:
        if yi > y_min:
            continue

        ans += 1
        y_min = yi

    print(ans)


if __name__ == "__main__":
    main()
