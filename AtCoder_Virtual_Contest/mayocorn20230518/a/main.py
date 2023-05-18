# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    st = [tuple(map(str, input().split())) for _ in range(n)]
    st = sorted(st, key=lambda x: int(x[1]), reverse=True)
    print(st[1][0])


if __name__ == "__main__":
    main()
