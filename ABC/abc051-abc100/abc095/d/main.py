# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    x = [0 for _ in range(n)]
    v = [0 for _ in range(n)]

    for i in range(n):
        xi, vi = map(int, input().split())
        x[i] = xi
        v[i] = vi

    def calc():
        from itertools import accumulate

        # 始めにいた位置→時計回りにaiまで移動したときの摂取カロリー
        a = list(accumulate(v))
        # 始めにいた位置→反時計回りにbiまで移動したときの摂取カロリー
        b = list(accumulate(v[::-1]))[::-1]

        # 反時計回りに移動したときの距離
        y = [c - xi for xi in x]

        # 反時計回りに移動したときの摂取カロリーの最大値
        d = [0 for _ in range(n)]
        d[n - 1] = b[n - 1] - y[n - 1]

        for i in range(n - 2, -1, -1):
            d[i] = b[i] - y[i]
            d[i] = max(d[i], d[i + 1])

        candidate = 0

        # aiの位置を全探索
        for i, (ai, xi) in enumerate(zip(a, x)):
            sum_cal = 0
            sum_cal -= xi  # walk
            sum_cal += ai  # eat

            candidate = max(candidate, sum_cal)

            # 最初の位置まで戻る
            sum_cal -= xi  # walk

            if i < n - 1:
                sum_cal += d[i + 1]

            candidate = max(candidate, sum_cal)

        return candidate

    ans = 0

    # O→A→O→B
    result = calc()
    ans = max(ans, result)

    # O→B→O→A
    v = v[::-1]
    x = [c - xi for xi in x][::-1]
    result = calc()
    ans = max(ans, result)

    print(ans)


if __name__ == "__main__":
    main()
