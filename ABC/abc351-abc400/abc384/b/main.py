# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, r = map(int, input().split())
    t = r

    for _ in range(n):
        di, ai = map(int, input().split())

        if di == 1 and (1600 <= t < 2800):
            t += ai
        elif di == 2 and (1200 <= t < 2400):
            t += ai

    print(t)


if __name__ == "__main__":
    main()
