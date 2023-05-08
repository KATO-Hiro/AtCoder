# -*- coding: utf-8 -*-


def main():
    import sys
    from typing import List

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    no_color, black, white = 0, 1, -1
    colors = [no_color] * n

    # See:
    # https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
    def is_bipartite(start_id: int):
        stack = [(start_id, black)]  # vertex, color
        # △: 連結成分内における2色の数を求める
        black_count, white_count = 0, 0

        while stack:
            vertex, color = stack.pop()

            # この判定は必要
            if colors[vertex] != no_color:
                continue

            colors[vertex] = color

            if color == black:
                black_count += 1
            elif color == white:
                white_count += 1

            for to in graph[vertex]:
                if colors[to] == color:
                    return False, 0, 0

                if colors[to] == no_color:
                    stack.append((to, -color))  # Invert colors.

        return True, black_count, white_count

    def nC2(n):
        return n * (n - 1) // 2

    ans = nC2(n) - m

    # 連結成分ごとに二部グラフか判定
    # 頂点のペア数 = 全体 - 条件を満たさない場合
    # nC2 - 白色で塗る頂点の個数wC2 - 黒色で塗る頂点の個数bC2 - 元々の辺の数m
    for i in range(n):
        if colors[i] != no_color:
            continue

        flag, black_count, white_count = is_bipartite(i)

        if flag:
            ans -= nC2(black_count)
            ans -= nC2(white_count)
        else:
            print(0)
            exit()

    print(ans)


if __name__ == "__main__":
    main()
