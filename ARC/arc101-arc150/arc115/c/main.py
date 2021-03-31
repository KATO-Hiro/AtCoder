# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = [2 for _ in range(n + 1)]
    ans[1] = 1

    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            ans[j] = max(ans[j], ans[i] + 1)

    print(*ans[1:])


if __name__ == "__main__":
    main()
