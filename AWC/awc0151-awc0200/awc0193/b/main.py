# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = -1
    value = -1

    for i, ai in enumerate(a, 1):
        if ai > value:
            ans = i
            value = ai

    print(ans)


if __name__ == "__main__":
    main()
