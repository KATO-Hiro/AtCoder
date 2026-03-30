# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    before = [0] * (m + 1)
    after = [0] * (m + 1)

    for _ in range(n):
        ai, bi = map(int, input().split())
        before[ai] += 1
        after[bi] += 1

    for i in range(1, m + 1):
        ans = after[i] - before[i]
        print(ans)


if __name__ == "__main__":
    main()
