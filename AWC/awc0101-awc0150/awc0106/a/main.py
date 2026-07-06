# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, k = map(int, input().split())
    h = [int(input()) for _ in range(n)]
    c = Counter()

    for i in range(k):
        c[h[i]] += 1

    if c[h[k - 1]] == k:
        print("Yes")
        exit()

    for j in range(k, n):
        c[h[j]] += 1
        c[h[j - k]] -= 1

        if c[h[j]] == k:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
