# -*- coding: utf-8 -*-


ans = 0


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        di = list(map(int, input().split()))

        for j, dij in enumerate(di):
            j += i + 1

            d[i][j] = dij
            d[j][i] = dij

    # print(d)
    if n % 2 == 1:
        n += 1  # 頂点が奇数の場合に、ダミーとなる頂点とペアを作ることに相当

    used = [False] * n

    def dfs(cur, weight):
        global ans
        ans = max(ans, weight)

        if cur == n:
            return
        if used[cur]:
            dfs(cur + 1, weight)
            return

        used[cur] = True

        for to in range(cur + 1, n):
            if used[to]:
                continue

            used[to] = True
            dfs(cur + 1, weight + d[cur][to])
            used[to] = False

        used[cur] = False

    dfs(0, 0)
    print(ans)


if __name__ == "__main__":
    main()
