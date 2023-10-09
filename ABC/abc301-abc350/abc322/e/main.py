# -*- coding: utf-8 -*-


def main():
    import sys
    from collections import defaultdict

    input = sys.stdin.readline

    n, k, p = map(int, input().split())
    inf = 10**18
    dp = defaultdict(lambda: inf)
    # listではなくtuple
    init_params = tuple([0] * k)
    dp[init_params] = 0

    for _ in range(n):
        ci, *a = map(int, input().split())
        ndp = defaultdict(lambda: inf)

        for params, cost in dp.items():
            new_params = [0] * k

            for i, (param, ai) in enumerate(zip(params, a)):
                new_params[i] = min(param + ai, p)

            # 選ばない
            ndp[params] = min(ndp[params], dp[params])

            # 選ぶ
            new_params = tuple(new_params)
            ndp[new_params] = min(ndp[new_params], dp[params] + ci)

        dp = ndp

    last_params = tuple([p] * k)
    ans = dp[last_params]

    if ans == inf:
        ans = -1

    print(ans)


if __name__ == "__main__":
    main()
