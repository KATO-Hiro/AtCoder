# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0

    for hi in h:
        if hi < x:
            continue

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
