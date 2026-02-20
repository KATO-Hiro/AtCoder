# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, k = map(int, input().split())
    s = list(map(int, input().split()))

    for _ in range(m):
        pi, vi = map(int, input().split())
        pi -= 1
        s[pi] = vi

    ans = 0

    for si in s:
        if si < k:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
