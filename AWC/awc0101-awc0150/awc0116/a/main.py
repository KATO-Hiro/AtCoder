# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    sum_a, sum_b = sum(a), sum(b)
    diff = sum_a - sum_b

    if diff >= 0:
        print("-1")
    else:
        print(-s // diff)


if __name__ == "__main__":
    main()
