# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a = [0 for _ in range(n)]
    max_a[0] = a[0]

    for i in range(1, n):
        max_a[i] = max(max_a[i - 1], a[i])

    ans = 0

    for max_ai, bi in zip(max_a, b):
        ans = max(ans, max_ai * bi)
        print(ans)


if __name__ == "__main__":
    main()
