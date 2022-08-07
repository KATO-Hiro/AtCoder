# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = n

    for key, value in c.items():
        if value >= 2:
            ans -= value - 1
            c[key] = 1

    if (n - sum(c.values())) % 2 == 1:
        ans -= 1

    print(ans)


if __name__ == "__main__":
    main()
