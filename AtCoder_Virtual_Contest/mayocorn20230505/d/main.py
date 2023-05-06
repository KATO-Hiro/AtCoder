# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    ans = 0

    # 絶対値を外す + 各変数を独立に扱えるように式変形
    # j - i = ai + aj
    # j - aj = i + ai

    # 片方を固定して、もう片方を高速化
    for j in range(n):
        ans += d[j - a[j]]
        d[j + a[j]] += 1
    
    print(ans)


if __name__ == "__main__":
    main()
