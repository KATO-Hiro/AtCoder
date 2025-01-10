# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0

    for ai in a:
        for bj in b:
            ans += ai * bj

    print(ans)


if __name__ == "__main__":
    main()
