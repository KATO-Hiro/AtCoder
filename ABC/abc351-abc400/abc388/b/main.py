# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    tl = [tuple(map(int, input().split())) for _ in range(n)]

    for k in range(1, d + 1):
        ans = 0

        for ti, li in tl:
            ans = max(ans, ti * (li + k))

        print(ans)


if __name__ == "__main__":
    main()
