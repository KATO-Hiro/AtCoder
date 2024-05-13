# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    waiting = 0

    for ai in a:
        if waiting + ai <= k:
            waiting += ai
        else:
            ans += 1
            waiting = ai

    if waiting > 0:
        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
