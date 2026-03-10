# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    ans = 0

    for _ in range(n):
        ai, bi = map(int, input().split())
        ai -= 1

        weight = min(c[ai], bi)
        ans += weight
        c[ai] -= weight

    print(ans)


if __name__ == "__main__":
    main()
