# -*- coding: utf-8 -*-


def main():
    from collections import Counter
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    b = Counter(a)
    diff = dict()
    total = 0

    # 余事象
    for key, value in b.items():
        comb1 = value * (value - 1) // 2
        comb2 = (value - 1) * (value - 2) // 2
        total += comb1
        diff[key] = max(0, comb1 - comb2)

    ans = [0 for _ in range(n)]

    for index, ai in enumerate(a):
        ans[index] = total - diff[ai]

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
