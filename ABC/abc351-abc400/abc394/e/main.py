# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    c = [list(input().rstrip()) for _ in range(n)]
    inf = 10**9
    dist = [[inf] * n for _ in range(n)]
    q = deque()

    def push(i, j, d):
        if dist[i][j] != inf:
            return

        dist[i][j] = d
        q.append((i, j))

    # 回文は先頭からではなく、中央から両端を伸ばすように処理すると楽
    # パスを頂点としたグラフと言い換え、多始点BFS の問題に帰着
    # 初期化: 対角線上は距離0、与えられたパスの距離は1
    for i in range(n):
        push(i, i, 0)

    for i in range(n):
        for j in range(n):
            if c[i][j] == "-":
                continue

            push(i, j, 1)

    while q:
        s, t = q.popleft()

        # 両端を伸ばせる、かつ、それらの文字が同じ場合のみ頂点を追加
        for ns in range(n):
            for nt in range(n):
                if c[ns][s] == "-":
                    continue
                if c[t][nt] == "-":
                    continue
                if c[ns][s] != c[t][nt]:
                    continue

                push(ns, nt, dist[s][t] + 2)

    for i in range(n):
        ans = list()

        for j in range(n):
            d = dist[i][j]

            if d == inf:
                d = -1

            ans.append(d)

        print(*ans)


if __name__ == "__main__":
    main()
