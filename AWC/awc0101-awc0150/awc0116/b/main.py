# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ab = [(bi - ai, i) for i, (ai, bi) in enumerate(zip(a, b))]
    ab.sort(reverse=True)
    ans = 0

    for i, (_, j) in enumerate(ab):
        if i < k:
            ans += b[j]
        else:
            ans += a[j]

    print(ans)


if __name__ == "__main__":
    main()
