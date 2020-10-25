# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    total = 0
    i = 0
    j = 0
    ans = 0

    for i in range(n):
        while total + a[j] <= n:
            total += a[j]

            if total == n:
                ans += 1

            if j >= n - 1:
                break

            j += 1

        total -= a[i]

    print(ans)


if __name__ == "__main__":
    main()
