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
    def is_bipartite(
        start_id: int,
        graph: List[List],
        colors: List[int],
        black_count: int = 0,
        white_count: int = 0,
    ):
        stack = [(start_id, black)]  # vertex, color

        while stack:
            vertex, color = stack.pop()

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

    def nC2(i: int) -> int:
        return i * (i - 1) // 2

    # 頂点のペア(全体) - 既に使われている辺の数
    ans = nC2(n) - m

    # 連結成分ごとにみる
    for i in range(n):
        if colors[i] != no_color:
            continue

        ok, black_count, white_count = is_bipartite(i, graph, colors)

        if ok:
            # print(black_count, white_count)
            ans -= nC2(black_count)
            ans -= nC2(white_count)
        else:
            ans = 0
            break

    print(ans)


if __name__ == "__main__":
    main()
