# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    t = list(map(int, input().split()))
    remain = 6000

    for ti in t:
        if ti == -1:
            print(-1)
            remain = -1
            continue

        remain -= ti

        if remain < 0:
            remain = -1

        print(remain)


if __name__ == "__main__":
    main()
