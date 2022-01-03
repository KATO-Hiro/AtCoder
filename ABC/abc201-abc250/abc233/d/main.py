# -*- coding: utf-8 -*-


def main():
    from itertools import accumulate
    from collections import Counter
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(accumulate(a))
    c = Counter()
    c[0] = 1
    ans = 0

    # See:
    # https://qiita.com/u2dayo/items/46b86ba21d7a98e765cd
    for si in s:
        ans += c[si - k]
        c[si] += 1
    
    print(ans)


if __name__ == "__main__":
    main()
