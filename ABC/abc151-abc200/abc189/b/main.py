# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    x *= 100
    total = 0
    count = 0

    for i in range(n):
        vi, pi = map(int, input().split())

        total += vi * pi
        count += 1

        if total > x:
            print(count)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
