# -*- coding: utf-8 -*-


def main():
    n = int(input())
    i = 1
    ans = 0

    # KeyInsight:
    # 桁ごとに周期性があることに気が付けるかどうか
    # 必ずしも桁DPにこだわる必要はない
    # See:
    # https://atcoder.jp/contests/abc029/submissions/4033702
    while i <= n:
        # 何周期あるか?
        ans += n // (i * 10) * i
        # 端数にどれだけ含まれているか?
        # この条件分岐のところが整理できていなかった
        # 該当なし、最大、「該当なし」より大きく〜「最大」より小さい
        ans += max(0, min(i, n % (i * 10) - i + 1))

        i *= 10

    print(ans)


if __name__ == '__main__':
    main()
