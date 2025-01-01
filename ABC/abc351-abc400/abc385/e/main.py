# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    degrees = [len(graph[i]) for i in range(n)]
    ans = n

    # 中心と葉の個数yを全探索
    for frm in range(n):
        d = []

        for to in graph[frm]:
            d.append(degrees[to])

        d.sort(reverse=True)

        for i, di in enumerate(d, 1):
            count = di * i + 1
            ans = min(ans, n - count)

    print(ans)


if __name__ == "__main__":
    main()
