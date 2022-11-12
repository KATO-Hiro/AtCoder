# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, b = map(int, input().split())
    a = list(map(int, input().split()))
    c = list(map(int, input().split()))

    ans = sum(c) * n
    ans += sum(a) * m
    ans += b * n * m
    print(ans)


if __name__ == "__main__":
    main()
