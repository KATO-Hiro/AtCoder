# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d, v = map(int, input().split())
    s = list(map(int, input().split()))
    ans = 0

    for si in s:
        if si > v:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
