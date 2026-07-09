# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, s, k = map(int, input().split())
    d = list(map(int, input().split()))
    ans = s + k * n + sum(d)
    print(ans)


if __name__ == "__main__":
    main()
