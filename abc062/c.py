# -*- coding: utf-8 -*-


# See:
# https://img.atcoder.jp/arc074/editorial.pdf
def calc(h, w):
    ans = float('inf')

    # Key Insight: ABCのC問題の基本は全探索
    # 分割方法は4通り
    # h, wを入れ替えれば実質2通り

    # 長方形Aの面積saを全探索
    for hi in range(1, h):
        sa = hi * w

        # 残りの長方形の扱い
        # 縦に2分割
        wi = w // 2
        sb = (h - hi) * wi
        sc = (h - hi) * (w - wi)
        ans = min(ans, max(sa, sb, sc) - min(sa, sb, sc))

        # 横に2分割
        hj = (h - hi) // 2
        sb = hj * w
        sc = (h - hi - hj) * w
        ans = min(ans, max(sa, sb, sc) - min(sa, sb, sc))

    return ans


def main():
    h, w = map(int, input().split())

    print(min(calc(h, w), calc(w, h)))


if __name__ == '__main__':
    main()
