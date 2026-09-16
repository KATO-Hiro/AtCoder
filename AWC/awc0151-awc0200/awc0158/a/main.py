# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, c = map(int, input().split())
    r = list(map(int, input().split()))
    ans = max(0, sum(r) - s) * c
    print(ans)


if __name__ == "__main__":
    main()
