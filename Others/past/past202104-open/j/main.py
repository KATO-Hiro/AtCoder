# -*- coding: utf-8 -*-


def main():
    from statistics import mean
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    x = [0 for _ in range(n)]
    ans = 0

    for i in range(n):
        xi, yi = map(int, input().split())
        x[i] = xi

        ans += abs(c - yi) ** 2

    x_mean = mean(x)
    ans += sum([abs(x_mean - xi) ** 2 for xi in x])

    print(ans)


if __name__ == "__main__":
    main()
