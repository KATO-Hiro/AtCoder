# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    h = list(map(int, input().split()))
    prev = -1
    ans = 0

    for hi in h:
        if hi > prev:
            prev = hi
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
