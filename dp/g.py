# -*- coding: utf-8 -*-


def main():
    # 再帰関数を使うときは，その上限回数に注意
    # https://docs.python.org/ja/3/library/sys.html#sys.setrecursionlimit
    from sys import setrecursionlimit

    setrecursionlimit(10 ** 7)

    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    # node vを始点としたときの，graphの有効パスの長さの最大値
    dp = [-1 for _ in range(n)]

    for _ in range(m):
        xi, yi = map(int, input().split())
        xi -= 1
        yi -= 1
        graph[xi].append(yi)

    # KeyInsight
    # DPの更新順序が非自明のとき，メモ化再帰が大きなメリットとなる
    # トポロジカルソートしながらDPしている
    # See:
    # https://qiita.com/drken/items/03c7db44ccd27820ea0d#g-%E5%95%8F%E9%A1%8C---longest-path
    def rec(v):
        # 更新済み
        if dp[v] != -1:
            return dp[v]

        result = 0

        for next_v in graph[v]:
            result = max(result, rec(next_v) + 1)

        # メモを更新
        dp[v] = result

        return dp[v]

    ans = 0

    for i in range(n):
        ans = max(ans, rec(i))

    print(ans)


if __name__ == '__main__':
    main()
