# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    for _ in range(n):
        li, ti = map(int, input().split())
        pi, ri = divmod(li, ti)

        if ri > 0 and ri >= ti // 2:
            pi += 1

        print(pi)


if __name__ == "__main__":
    main()
