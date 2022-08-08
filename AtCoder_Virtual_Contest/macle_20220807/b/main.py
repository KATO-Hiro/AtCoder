# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    from itertools import accumulate
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(accumulate([0] + a))
    d = defaultdict(int)
    ans = 0

    # rを固定して、分布として管理
    for left in range(n + 1):
        ans += d[s[left]]
        d[s[left] + k] += 1

    print(ans)


if __name__ == "__main__":
    main()
