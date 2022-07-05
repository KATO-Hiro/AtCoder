# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans = 0

    for key in c.keys():
        ans = max(ans, c[key - 1] + c[key] + c[key + 1])

    print(ans)


if __name__ == "__main__":
    main()
