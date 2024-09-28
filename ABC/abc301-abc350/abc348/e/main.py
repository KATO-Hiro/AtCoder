# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(5 * 10**6)

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    c = list(map(int, input().split()))
    c_total = sum(c)
    center = -1

    # 木の重心を求める問題に帰着
    # = 部分木のコストの総和が全体の半分以下であるものを見つける、と言い換え
    def dfs(cur, parent=-1) -> int:
        nonlocal center

        c_summed = c[cur]
        c_max = 0

        for to in graph[cur]:
            if to == parent:
                continue

            now = dfs(to, cur)
            c_max = max(c_max, now)
            c_summed += now

        # 戻りがけの判定も必要
        c_max = max(c_max, c_total - c_summed)

        # 木の重心となる頂点
        if c_max * 2 <= c_total:
            center = cur

        return c_summed

    dfs(0)
    # print(center)

    ans = 0

    def f(cur, parent=-1, dist=0):
        nonlocal ans

        ans += c[cur] * dist

        for to in graph[cur]:
            if to == parent:
                continue

            f(to, cur, dist + 1)

    f(center)
    print(ans)


if __name__ == "__main__":
    main()
