# -*- coding: utf-8 -*-


def main():
    n, r = map(int, input().split())
    s = list(input())

    # See:
    # https://www.slideshare.net/chokudai/arc040
    # Key Insight
    # 2つの操作を独立に扱う

    # 1.移動に必要な時間
    # 最も右にある'.'を塗ることができる位置まで移動できればよい
    pos = 0

    for index, si in enumerate(s, 1):
        if si == '.':
            pos = index

    move_count = max(0, pos - r)

    # 2.銃を撃つ（マスを塗る）回数
    shot_count = 0

    for index, si in enumerate(s):
        # 最も左にある'.'（マスiとする）を探す
        if si == '.':
            shot_count += 1

            # マスi～マスi + R - 1までを塗る
            for j in range(index, min(index + r, n)):
                s[j] = 'o'

    # 移動と銃撃にかかる時間の合計が答え
    ans = move_count + shot_count
    print(ans)


if __name__ == '__main__':
    main()
