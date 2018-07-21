# -*- coding: utf-8 -*-
# AtCoder Beginner Contest


if __name__ == '__main__':
    from statistics import median

    n = int(input())
    a = list(map(int, input().split()))
    total = 0

    # See:
    # https://www.youtube.com/watch?v=UX4AuiCVtN4
    # https://beta.atcoder.jp/contests/abc102/submissions/2768315
    mod_a = sorted([ai - i for i, ai in enumerate(a, 1)])
    b = median(mod_a)

    for i in range(n):
        total += abs(mod_a[i] - b)

    print(int(total))
