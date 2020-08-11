# -*- coding: utf-8 -*-


def calc_dist(s, start_i, start_j, h, w):
    from collections import deque

    result = 0
    # 待ち行列に相当する部分をキューで管理
    d = deque()
    # キューの初期化
    d.append((start_i, start_j))
    # 仮決めした始点からの距離を計算
    dist = [[0 for _ in range(w)] for _ in range(h)]
    # 迷路のマスを通ったかどうかを管理
    visited = [[False for _ in range(w)] for _ in range(h)]
    visited[start_i][start_j] = True
    # 4方向を移動する部分を配列でスマートに管理する
    dxy = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while d:
        hd, wd = d.popleft()

        # 上下左右の4方向に移動
        for dx, dy in dxy:
            nx = wd + dx
            ny = hd + dy

            # 迷路の範囲外
            if nx < 0 or nx >= w or ny < 0 or ny >= h:
                continue

            # 壁
            if s[ny][nx] == '#':
                continue

            # 既に通過した
            # DEBUG: 本番では、ここがなくて計算量が爆発していた
            if visited[ny][nx]:
                continue

            visited[ny][nx] = True
            dist[ny][nx] = dist[hd][wd] + 1
            d.append((ny, nx))
            result = max(result, dist[ny][nx])

    return result


def main():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]
    ans = 0

    # KeyInsight
    # 始点のみを全探索(終点は全探索する必要はない．終点の位置は、移動距離の最大値に相当)
    # 距離は幅優先探索BFSで計算
    # DEBUG: 終点を全探索するループさえなければACしていた
    for start_i in range(h):
        for start_j in range(w):
            # 始点が壁のときは、距離を計算しない
            if s[start_i][start_j] == '#':
                continue

            ans = max(ans, calc_dist(s, start_i, start_j, h, w))

    print(ans)


if __name__ == '__main__':
    main()
