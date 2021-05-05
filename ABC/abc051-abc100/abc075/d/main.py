# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    x = [0 for _ in range(n)]
    y = [0 for _ in range(n)]

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi
        y[i] = yi

    sx = sorted(x)
    sy = sorted(y)

    ans = float("inf")

    for xi in range(n):
        for xj in range(xi + 1, n):
            for yi in range(n):
                for yj in range(yi + 1, n):
                    count = 0

                    x_min = sx[xi]
                    x_max = sx[xj]
                    y_min = sy[yi]
                    y_max = sy[yj]

                    for p in range(n):
                        if x_min <= x[p] <= x_max and y_min <= y[p] <= y_max:
                            count += 1

                    if count >= k:
                        ans = min(ans, (x_max - x_min) * (y_max - y_min))

    print(ans)


if __name__ == "__main__":
    main()
