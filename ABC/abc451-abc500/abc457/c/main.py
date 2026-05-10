# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = []

    for _ in range(n):
        __, *ai = map(int, input().split())
        a.append(ai)

    c = list(map(int, input().split()))
    remain = k

    for ai, ci in zip(a, c):
        size = len(ai)
        count = size * ci

        if count < remain:
            remain -= count
        else:
            remain -= 1
            remain %= size
            print(ai[remain])
            break


if __name__ == "__main__":
    main()
