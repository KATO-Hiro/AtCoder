# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    ans = 0

    # KeyInsight:
    # j - i = Ai + Aj (j > i)、条件つきで絶対値の記号を外す
    # ▲: 計算量を落とす: 片方を固定して、考えられないか?
    # 左辺・右辺を独立として考えられないか?
    # See:
    # https://www.youtube.com/watch?v=OCRLlMa7kL0&feature=youtu.be
    for i in range(n):
        # jまでにiがどれだけ条件を満たすかを判定している
        # Ai + i = j - Aj
        # jの計算に相当
        diff = i - a[i]
        ans += d[diff]

        # iの計算に相当
        summed = i + a[i]
        d[summed] += 1

    print(ans)


if __name__ == '__main__':
    main()
