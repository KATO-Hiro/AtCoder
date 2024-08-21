# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    d = defaultdict(list)

    for ai, wi in zip(a, w):
        d[ai].append(wi)

    ans = 0

    for values in d.values():
        ans += sum(values) - max(values)

    print(ans)


if __name__ == "__main__":
    main()
