# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s = map(int, input().split())
    w = list(map(int, input().split()))
    ans = 0
    now = 0

    for wi in w:
        now += wi

        if now >= s:
            ans += 1
            now = 0

    print(ans)


if __name__ == "__main__":
    main()
