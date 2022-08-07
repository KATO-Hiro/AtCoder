# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    same_count = 0
    ans = 0

    for i, ai in enumerate(a, 1):
        if i == ai:
            same_count += 1
        else:
            if (ai, i) in d.keys():
                d[(ai, i)] += 1
            else:
                d[(i, ai)] = 1

    ans = same_count * (same_count - 1) // 2

    for value in d.values():
        if value >= 2:
            ans += 1

    print(ans)
    

if __name__ == "__main__":
    main()
