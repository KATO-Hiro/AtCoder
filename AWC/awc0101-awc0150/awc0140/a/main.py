# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]

    for i in range(1, n):
        if a[i] > a[i - 1]:
            ans += 2 * a[i]
        else:
            ans += a[i]

    print(ans)


if __name__ == "__main__":
    main()
