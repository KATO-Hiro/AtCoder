# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    s = [input().rstrip() for _ in range(n)]

    # 頂点1→頂点v、頂点v→頂点nを前計算
    inf = 10**12
    dist_1v = [inf] * n
    dist_vn = [inf] * n
    dist_1v[0], dist_vn[n - 1] = 0, 0

    for i in range(n):
        for j in range(m):
            if s[i][j] == "0":
                continue

            dist_1v[i + j + 1] = min(dist_1v[i + j + 1], dist_1v[i] + 1)

    for i in range(n - 1, -1, -1):
        for j in range(m):
            if s[i][j] == "0":
                continue

            dist_vn[i] = min(dist_vn[i], dist_vn[i + j + 1] + 1)

    ans = list()

    # 頂点kをスキップするような頂点を探索
    # 左側: [k - m, k)、右側[k + 1, k + 1 + m)
    for k in range(1, n - 1):
        candidate = inf

        for left in range(k - m, k):
            if left < 0:
                continue

            for right in range(k + 1, k + 1 + m):
                if right >= n or (right - left) > m:
                    break

                if s[left][right - left - 1] == "0":
                    continue

                candidate = min(candidate, dist_1v[left] + dist_vn[right] + 1)

        if candidate == inf:
            candidate = -1

        ans.append(candidate)

    print(*ans)


if __name__ == "__main__":
    main()
