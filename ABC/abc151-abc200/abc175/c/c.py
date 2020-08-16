# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    x, k, d = map(int, input().split())
    x = abs(x)
    kd = k * d

    # See:
    # https://www.youtube.com/watch?v=auQRcs5JMwE&feature=youtu.be
    # KeyInsight:
    # △: 対称性から、x>=0の場合を考えれば良い。実装も楽になる。

    if kd <= x:
        # ◯: 原点付近で往復する前に、シミュレーションが終わる。
        print(x - kd)
    else:
        # ◯: 原点付近で往復する
        count = x // d
        k_dash = k - count  # 残りの移動回数
        x -= count * d

        # △: 移動回数の残りが偶奇で変わる
        if k_dash % 2 == 0:
            print(x)
        else:
            print(d - x)


if __name__ == '__main__':
    main()
