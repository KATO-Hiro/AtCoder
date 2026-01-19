# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a, reverse=True)
    total = 0

    for i in range(n - k, n):
        total += a[i]

        if total >= x:
            print(i + 1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
