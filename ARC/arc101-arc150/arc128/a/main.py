# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n

    for i in range(n - 1):
        if a[i] <= a[i + 1]:
            continue

        ans[i] ^= 1
        ans[i + 1] ^= 1

    print(*ans)


if __name__ == "__main__":
    main()
