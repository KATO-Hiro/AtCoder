# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    a_max = max(a)
    ans = 0

    for ai in a:
        ans += a_max - ai

    print(ans)


if __name__ == "__main__":
    main()
