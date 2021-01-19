# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]

    ans = float("inf")

    for ns in range(h):
        for ew in range(w):
            dist = 0

            for i in range(h):
                for j in range(w):
                    dist += a[i][j] * min(abs(i - ns), abs(j - ew))

            ans = min(ans, dist)

    print(ans)


if __name__ == "__main__":
    main()
