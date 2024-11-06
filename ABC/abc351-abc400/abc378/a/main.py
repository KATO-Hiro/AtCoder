# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import Counter

    input = sys.stdin.readline

    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for values in c.values():
        ans += values // 2

    print(ans)


if __name__ == "__main__":
    main()
