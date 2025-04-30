# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, d = map(int, input().split())
    a = list(map(int, input().split()))

    # コーナーケース
    if d == 0:
        # 重複なし
        ans = n - len(set(a))
        print(ans)
        exit()

    size = 10**6 + 10
    freq = [0] * size

    # 頻度分布を求める
    for ai in a:
        freq[ai] += 1

    def solve(array):
        size = len(array)
        # i番目まで決めたときに、直前の要素を選ばない/選んだときの最大値
        dp = [0] * 2

        for ai in array:
            ndp = [0] * 2

            ndp[0] = max(ndp[0], dp[0], dp[1])
            ndp[1] = max(ndp[1], dp[0] + ai)

            dp = ndp

        result = max(dp)

        return sum(array) - result

    # 周期dで独立に考える
    ans = 0

    for i in range(d):
        b = list()

        for j in range(i, size, d):
            b.append(freq[j])

        ans += solve(b)

    print(ans)


if __name__ == "__main__":
    main()
