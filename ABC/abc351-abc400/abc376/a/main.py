# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    t = list(map(int, input().split()))
    inf = 10**9
    prev = -inf
    ans = 0

    for ti in t:
        if prev + c <= ti:
            ans += 1
            prev = ti

    print(ans)


if __name__ == "__main__":
    main()
