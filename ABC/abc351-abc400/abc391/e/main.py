# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = input().rstrip()
    m = len(s)
    # # 木dp: dp[v][i]: 頂点vにおいて、0もしくは1にするときのコストの最小値
    dp = [[1 for _ in range(2)] for _ in range(m)]

    # 元の01列と同じ場合のコストは0
    for i, si in enumerate(s):
        dp[i][int(si)] = 0

    inf = 10**18

    while len(dp) > 1:
        size = len(dp)
        ndp = [[inf for _ in range(2)] for _ in range(size // 3)]

        # 部分木を3つずつ見る
        for left in range(0, size, 3):
            for pattern in range(1 << 3):
                cost = 0

                for delta in range(3):
                    cost += dp[left + delta][pattern >> delta & 1]

                # 多数決をpopcountで判定
                majority = 1 if pattern.bit_count() >= 2 else 0
                ndp[left // 3][majority] = min(ndp[left // 3][majority], cost)

        dp = ndp

    ans = max(dp[0])
    print(ans)


if __name__ == "__main__":
    main()
