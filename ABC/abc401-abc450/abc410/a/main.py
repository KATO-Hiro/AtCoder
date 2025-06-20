# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    ans = 0

    for ai in a:
        if k <= ai:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
