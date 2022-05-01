# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    n_max = 12
    box = [0] * m
    cost = [0] * m

    # See:
    # https://blog.hamayanhamayan.com/entry/2019/09/28/230624
    for i in range(m):
        ai, bi = map(int, input().split())
        c = list(map(int, input().split()))
        cost[i] = ai

        # 各鍵で開けることができる宝箱を集合として管理
        for ci in c:
            ci -=1
            box[i] |= 1 << ci
    
    inf = 10 ** 9
    dp = [inf] * (1 << n_max)
    dp[0] = 0

    for i in range(m):
        ndp = [inf] * (1 << n_max)

        for mask in range(1 << n):
            # 鍵を選ばない
            ndp[mask] = min(ndp[mask], dp[mask])

            # 鍵を選ぶ
            new_mask = mask | box[i]
            ndp[new_mask] = min(ndp[new_mask], dp[mask] + cost[i])

        dp = ndp
    
    ans = dp[(1 << n) - 1]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
