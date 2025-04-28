# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i, ai in enumerate(a):
        if i % 2 == 0:
            ans += ai

    print(ans)


if __name__ == "__main__":
    main()
