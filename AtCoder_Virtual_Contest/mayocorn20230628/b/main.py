# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    c = sorted(list(map(int, input().split())))
    mod = 10**9 + 7
    ans = 1

    for i, ci in enumerate(c):
        ans *= max(0, ci - i)
        ans %= mod

    print(ans)


if __name__ == "__main__":
    main()
