# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for ai in a:
        prev = ai - 1

        if prev in d.keys():
            d[ai] = max(d[ai], d[prev] + 1)
        else:
            d[ai] = 1

    ans = max(d.values())
    print(ans)


if __name__ == "__main__":
    main()
