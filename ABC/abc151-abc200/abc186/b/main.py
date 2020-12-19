# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    min_value = float("inf")

    for i in range(h):
        for j in range(w):
            min_value = min(min_value, a[i][j])

    ans = 0

    for i in range(h):
        for j in range(w):
            ans += a[i][j] - min_value

    print(ans)


if __name__ == "__main__":
    main()
