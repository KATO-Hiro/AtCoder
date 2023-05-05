# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict
    import sys

    input = sys.stdin.readline

    h, w, n = map(int, input().split())
    d = defaultdict(list)
    ids = defaultdict(int)

    # See:
    # https://www.youtube.com/watch?v=KMsEXLe_8go
    for i in range(n):
        ri, ci, ai = map(int, input().split())
        d[-ai].append((ri, ci))  # キーを降順にするため-1倍
        ids[(ri, ci)] = i  # 座標ri, ciが何番目か記録
    
    row_max = defaultdict(int)
    col_max = defaultdict(int)
    ans = [0] * n
    
    for key in sorted(d.keys()):
        # aiが同じ場合に対処するため、移動回数の取得・更新を分ける
        # 取得
        for ri, ci in d[key]:
            now = max(row_max[ri], col_max[ci])
            ans[ids[(ri, ci)]] = now

        # 更新
        for ri, ci in d[key]:
            now = ans[ids[(ri, ci)]]
            row_max[ri] = max(row_max[ri], now + 1)
            col_max[ci] = max(col_max[ci], now + 1)
    
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
