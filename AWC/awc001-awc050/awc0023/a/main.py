# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, r = map(int, input().split())
    t = list(map(int, input().split()))
    ans = sum(t) + m * r
    print(ans)


if __name__ == "__main__":
    main()
