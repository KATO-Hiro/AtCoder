# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = [0] * m

    for _ in range(n):
        xi = list(map(int, input().split()))

        for i, xi in enumerate(xi):
            b[i] += xi

    ans = "Yes"

    for ai, bi in zip(a, b):
        if ai > bi:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    main()
