# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    h, w, m = map(int, input().split())
    h_count = [0 for _ in range(h)]
    w_count = [0 for _ in range(w)]
    pairs = set()

    # KeyInsight:
    # x方向とy方向を独立に考える
    # 爆破できる数: x方向の最大値 + y方向の最大値
    #             x, y方向が交差する場合は-1
    for i in range(m):
        hi, wi = map(int, input().split())
        hi -= 1
        wi -= 1

        h_count[hi] += 1
        w_count[wi] += 1

        pairs.add((hi, wi))

    # 各方向の最大値を計算
    h_max = max(h_count)
    w_max = max(w_count)
    hk = list()
    wk = list()

    # 各方向で、最大値となる行もしくは列を抽出
    for index, hj in enumerate(h_count):
        if hj == h_max:
            hk.append(index)

    for index, wj in enumerate(w_count):
        if wj == w_max:
            wk.append(index)

    # 答えの候補
    ans = h_max + w_max

    # 範囲を限定して全探索
    # 合計が最大値となる組み合わせを全探索
    for _h in hk:
        for _w in wk:
            hw = (_h, _w)

            if hw in pairs:
                continue

            # 一つでも条件に合致したら、計算を打ち切る
            print(ans)
            exit()

    print(ans - 1)


if __name__ == '__main__':
    main()
