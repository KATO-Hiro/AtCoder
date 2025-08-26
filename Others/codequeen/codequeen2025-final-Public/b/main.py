# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for key in sorted(c.keys()):
        if s < key or s > key * 2:
            continue
        elif s == key * 2:
            ci = c[key]
            ans += ci * (ci - 1) // 2
        else:
            ans += c[key] * c[s - key]

    print(ans)


if __name__ == "__main__":
    main()
