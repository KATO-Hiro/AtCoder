# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ans = "Yes"

    for i in range(n):
        if a[2 * i + 1] - a[2 * i] > d:
            ans = "No"
            break

    print(ans)


if __name__ == "__main__":
    main()
