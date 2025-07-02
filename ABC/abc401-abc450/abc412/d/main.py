# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import combinations

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai][bi] = 1
        graph[bi][ai] = 1

    edges = list(combinations(range(n), 2))
    ans = 10**18

    # M本の辺からN本の辺を選ぶ問題、と言い換え
    for selected_edges in combinations(edges, n):
        degrees = [0] * n

        for ui, vi in selected_edges:
            degrees[ui] += 1
            degrees[vi] += 1

        ok = all(degree == 2 for degree in degrees)

        if not ok:
            continue

        # 追加する辺の本数N、削除する可能性がある辺の本数M、共通する辺の本数
        ans = min(ans, n + m - 2 * sum(graph[ui][vi] for ui, vi in selected_edges))

    print(ans)


if __name__ == "__main__":
    main()
