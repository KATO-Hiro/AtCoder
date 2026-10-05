# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    p, q = divmod(m, n)
    ans = [p] * n

    for i in range(q):
        ans[i] += 1

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
