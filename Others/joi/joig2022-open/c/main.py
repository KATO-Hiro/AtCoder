# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [0] * (n + 1)

    for i in range(1, n + 1):
        xi, yi = map(int, input().split())
        ans[i] = ans[i - 1]

        if yi == 0:
            ans[i] += 1
        elif ans[i - 1] - ans[i - 1 - xi] >= yi:
            ans[i] += 1

    print(ans[n])


if __name__ == "__main__":
    main()
