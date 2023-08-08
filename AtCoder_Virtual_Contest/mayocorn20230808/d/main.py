# -*- coding: utf-8 -*-

ans = set()


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

    def dfs(cur, pairs, used):
        if cur == n:
            results = 0

            for pair in pairs:
                i, j = pair
                results ^= a[i][j]

            return results

        id = -1
        results = 0

        for i, u in enumerate(used):
            if not u:
                id = i
                break

        used[id] = True

        for j in range(id + 1, n2):
            if used[j]:
                continue

            pairs.append([id, j])
            used[j] = True
            results = max(results, dfs(cur + 1, pairs, used))
            pairs.pop()
            used[j] = False

        used[id] = False

        return results

    used = [False] * n2
    results = dfs(0, [], used)
    print(results)


if __name__ == "__main__":
    main()
