# -*- coding: utf-8 -*-

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    x -= 1
    y -= 1
    inf = 10 ** 7
    ans = [0 for _ in range(n)]

    # See:
    # https://www.youtube.com/watch?v=zG1L4vYuGrg&feature=youtu.be
    # KeyInsight:
    # △: 全探索 + 深さ優先探索
    # ×: どのように実装すればいいか、見当がつかなかった
    for i in range(n):
        # グラフを陽に持たない場合
        # 始点からの距離を管理
        dist = [inf for _ in range(n)]  # 距離無限大で初期化
        dist[i] = 0

        # キューを用意して、頂点を管理
        d = deque()
        d.append(i)

        # BFS
        while d:
            v = d.popleft()  # 最も左側の内容(=最初に突っ込んだ値)を取り出す
            dj = dist[v]

            # 場合分け
            # 範囲外参照を回避しながら、次の頂点に移動したときの距離を計算
            if v - 1 >= 0 and dist[v - 1] == inf:
                dist[v - 1] = dj + 1
                # 次の頂点をキューに突っ込む
                d.append(v - 1)
            if v + 1 < n and dist[v + 1] == inf:
                dist[v + 1] = dj + 1
                d.append(v + 1)
            if v == x and dist[y] == inf:
                dist[y] = dj + 1
                d.append(y)
            if v == y and dist[x] == inf:
                dist[x] = dj + 1
                d.append(x)

        # 距離ごとの個数を計算
        for j in range(n):
            ans[dist[j]] += 1

    # 始点と終点を区別
    for k in range(n):
        ans[k] //= 2

    # 答えを出力
    for ii in range(1, n):
        print(ans[ii])


if __name__ == '__main__':
    main()
