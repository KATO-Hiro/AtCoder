# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    ans = n

    for i, hi in enumerate(h, 1):
        if m - hi < 0:
            ans = i - 1
            break

        m -= hi

    print(ans)


if __name__ == "__main__":
    main()
