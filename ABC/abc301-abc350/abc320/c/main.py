# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m = int(input())
    s = [list(input().rstrip()) * 10 for _ in range(3)]
    inf = 10**18
    ans = inf
    n = 3 * m  # 所要時間の上限 = 1周で1つのリールを止める

    # 全てのリールを止めるまでの時間を全探索
    # 条件: 表示されている文字が全て同じ、かつ、各リールを止める時間が異なる
    # 計算量: O(m ** 3)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j:
                    continue
                if j == k:
                    continue
                if k == i:
                    continue

                if s[0][i % m] != s[1][j % m]:
                    continue
                if s[1][j % m] != s[2][k % m]:
                    continue
                if s[2][k % m] != s[0][i % m]:
                    continue

                ans = min(ans, max(i, j, k))

    # 例外処理
    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
