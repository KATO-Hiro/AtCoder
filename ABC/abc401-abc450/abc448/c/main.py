# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    size = min(len(c), 6)
    keys = sorted(c.keys())[:size]

    for i in range(q):
        _ = int(input())
        b = list(map(int, input().split()))

        for bi in b:
            value = a[bi - 1]
            c[value] -= 1

        for key in keys:
            if c[key] <= 0:
                continue

            ans = key
            print(ans)
            break

        for bi in b:
            value = a[bi - 1]
            c[value] += 1


if __name__ == "__main__":
    main()
