# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = sorted([(ai, i) for i, ai in enumerate(a, 1)])
    ans = [0] * (2 * n + 2)

    for ai, i in b:
        ans[2 * i] += ans[ai] + 1
        ans[2 * i + 1] += ans[ai] + 1

    print(*ans[1:], sep="\n")


if __name__ == "__main__":
    main()
