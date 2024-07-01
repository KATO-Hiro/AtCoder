# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    d = defaultdict(list)
    ans = 0

    for ai, wi in zip(a, w):
        d[ai].append(wi)

    for value in d.values():
        ans += sum(value) - max(value)

    print(ans)


if __name__ == "__main__":
    main()
