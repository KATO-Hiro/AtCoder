# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b_min = min(b)
    ans = 0

    for ai in a:
        if b_min >= ai:
            b_min -= ai
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
