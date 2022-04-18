# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    ans_min = float("inf")
    ans_max = 0

    for value in c.values():
        ans_min = min(ans_min, value)
        ans_max = max(ans_max, value)

    if len(c.keys()) != m:
        ans_min = 0
    
    print(ans_min, ans_max)


if __name__ == "__main__":
    main()
