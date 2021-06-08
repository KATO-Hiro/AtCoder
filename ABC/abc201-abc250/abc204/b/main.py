# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for ai in a:
        ans += max(0, (ai - 10))

    print(ans)


if __name__ == "__main__":
    main()
