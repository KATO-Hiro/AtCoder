# -*- coding: utf-8 -*-


def main():
    import sys
    from functools import lru_cache

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for i in range(1, n):
        bi = int(input())
        bi -= 1

        graph[bi].append(i)

    # 戻り値: 社員の給料
    @lru_cache(maxsize=None)
    def dfs(cur):
        # 基本ケース: 部下が一人もいない = 葉
        if len(graph[cur]) == 0:
            return 1

        # 再帰ケース
        value_min, value_max = 10**9, 0

        for to in graph[cur]:
            value = dfs(to)
            # 帰りがけ順
            value_min = min(value_min, value)
            value_max = max(value_max, value)

        return value_max + value_min + 1

    print(dfs(0))


if __name__ == "__main__":
    main()
