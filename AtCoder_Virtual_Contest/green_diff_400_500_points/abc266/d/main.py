# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    inf = 10**18
    dp = [-inf] * 5
    dp[0] = 0
    prev_t = 0

    for _ in range(n):
        ti, xi, ai = map(int, input().split())
        ndp = [-inf] * 5

        for cur in range(5):
            for to in range(5):
                # 時間差から移動できる範囲を絞る
                if abs(to - cur) > ti - prev_t:
                    continue

                ndp[to] = max(ndp[to], dp[cur] + ai * (to == xi))

        prev_t = ti
        dp = ndp

    print(max(dp))


if __name__ == "__main__":
    main()
