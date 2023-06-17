# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    ans = 0

    for i, ai in enumerate(a):
        ans += ai * (2**i)

    print(ans)


if __name__ == "__main__":
    main()
