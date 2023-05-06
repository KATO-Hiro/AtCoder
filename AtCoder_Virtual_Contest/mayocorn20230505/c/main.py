# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    c = list()

    for ai, bi in ab:
        for _ in range(bi):
            c.append(ai)

    # dp[i][j]: 硬貨をi枚使って、j円にできるか?
    # 部分和問題 + 枚数の分だけ状態が増える
    size_max = 10 ** 4 + 105
    dp = [False for _ in range(size_max)]
    dp[0] = True

    for ci in c:
        ndp = [False for _ in range(size_max)]

        for i in range(x + 1):
            if not dp[i]:
                continue

            # ciを選ばない
            ndp[i] = True
            # ciを選ぶ
            ndp[i + ci] = True

        dp = ndp
    
    if dp[x]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
