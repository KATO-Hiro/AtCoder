# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list()
    b = list()

    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)

    ans = float("inf")

    for i in range(n):
        for j in range(n):
            if i == j:
                ans = min(ans, a[i] + b[j])
            else:
                ans = min(ans, max(a[i], b[j]))

    print(ans)


if __name__ == "__main__":
    main()
