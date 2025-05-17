# -*- coding: utf-8 -*-


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n, k = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(n - 1):
        ai, bi = map(int, input().split())
        ai -= 1
        bi -= 1

        graph[ai].append(bi)
        graph[bi].append(ai)

    a = list(map(int, input().split()))
    inf = 10**18

    def dfs(cur, parent=-1):
        dp0 = [-inf] * (k + 1)  # 頂点iを選ばない
        dp1 = [-inf] * (k + 1)  # 頂点iを必ず選ぶ
        dp0[0] = 0
        dp1[1] = a[cur]

        for to in graph[cur]:
            if to == parent:
                continue

            cdp0, cdp1 = dfs(to, cur)
            ndp0 = [-inf] * (k + 1)
            ndp1 = [-inf] * (k + 1)

            for i in range(k + 1):
                for j in range(k + 1):
                    if i + j > k:
                        continue

                    if dp0[i] != -inf and cdp0[j] != -inf:
                        ndp0[i + j] = max(ndp0[i + j], dp0[i] + cdp0[j])
                    if dp0[i] != -inf and cdp1[j] != -inf:
                        ndp0[i + j] = max(ndp0[i + j], dp0[i] + cdp1[j])
                    if dp1[i] != -inf and cdp0[j] != -inf:
                        ndp1[i + j] = max(ndp1[i + j], dp1[i] + cdp0[j])

            dp0, dp1 = ndp0, ndp1

        return dp0, dp1

    dp0, dp1 = dfs(0)
    ans = max(dp0[k], dp1[k])

    if ans == -inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
