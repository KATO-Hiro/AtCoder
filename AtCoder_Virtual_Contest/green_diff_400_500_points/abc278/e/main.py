# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    h, w, n, hi, wj = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    d = defaultdict(int)

    for i in range(h):
        for j in range(w):
            d[a[i][j]] += 1

    ans = list()

    # 1回のみ全体を計算 + 差分を更新
    for k in range(h - hi + 1):
        dij = defaultdict(int)
        candidates = list()

        for i in range(k, k + hi):
            for j in range(wj):
                dij[a[i][j]] += 1

        count = 0

        for key, value in d.items():
            if value - dij[key] > 0:
                count += 1

        candidates.append(count)

        for x in range(wj, w):
            count = 0

            for y in range(k, k + hi):
                dij[a[y][x]] += 1
                dij[a[y][x - wj]] -= 1

            for key, value in d.items():
                if value - dij[key] > 0:
                    count += 1

            candidates.append(count)

        ans.append(candidates)

    for ans_i in ans:
        print(*ans_i)


if __name__ == "__main__":
    main()
