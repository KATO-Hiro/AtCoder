# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for value in c.values():
        ans += value * (value - 1) * (value - 2) // 6

    print(ans)


if __name__ == "__main__":
    main()
