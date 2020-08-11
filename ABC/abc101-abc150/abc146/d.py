# -*- coding: utf-8 -*-


def main():
    # 再帰の上限回数のデフォルトを変更
    from sys import setrecursionlimit
    setrecursionlimit(10 ** 7)

    n = int(input())
    graph = [list() for _ in range(n)]
    ans = [0 for _ in range(n - 1)]

    # KeyInsight:
    # 木の問題と再帰関数は相性がいい
    # See:
    # https://www.youtube.com/watch?v=7IlBVSglZqc
    for i in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1
        graph[ai].append((bi, i))
        graph[bi].append((ai, i))

    # 実装できなかったところ
    # 1. 色のカウントをどう管理するか?
    # 2. 辺のidをどう管理するか?

    # 親方向からの色番号を引数に持つ
    def dfs(vertex, parent=-1, edge_color=-1):
        # 一般的なポイント: 頂点に関する処理を書く
        color_code = 1

        # 基本形: 親の頂点周りを探索
        for to, edge_id in graph[vertex]:
            if to == parent:
                continue

            # 一般的なポイント: 辺に関する処理を書く
            if color_code == edge_color:
                color_code += 1

            ans[edge_id] = color_code
            color_code += 1

            dfs(to, vertex, ans[edge_id])
            # 一般的なポイント: 辺に関する処理を書く

        # 一般的なポイント: 頂点に関する処理を書く

    dfs(0)
    count = 0

    for g in graph:
        count = max(count, len(g))

    print(count)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
