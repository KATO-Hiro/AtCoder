# -*- coding: utf-8 -*-

ans = 0


def main():
    import sys

    sys.setrecursionlimit(10**8)

    input = sys.stdin.readline

    n = int(input())
    n2 = n * 2
    a = list()

    for i in range(2 * n):
        ai = [0] * (i + 1) + list(map(int, input().split()))
        a.append(ai)

    def dfs(cur, total, used):
        global ans

        if cur == n:
            ans = max(ans, total)
            return

        id = -1

        for i, u in enumerate(used):
            if not u:
                id = i
                used[id] = True
                break

        for j in range(id + 1, n2):
            if used[j]:
                continue

            used[j] = True
            dfs(cur + 1, total ^ a[id][j], used)
            used[j] = False

        used[id] = False

    used = [False] * n2
    dfs(0, 0, used)
    print(ans)


if __name__ == "__main__":
    main()
