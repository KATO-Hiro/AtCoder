# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = 0

    for i in range(1, n - 1):
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
