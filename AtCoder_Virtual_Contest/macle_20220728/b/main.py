# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    s = sorted([int(input()) for _ in range(n)], reverse=True)
    ans = 0
    size_max = 10 ** 4 + 10
    # 状態として、得点そのものを持つ
    dp = [False] * size_max
    dp[0] = True

    # See:
    # https://blog.hamayanhamayan.com/entry/2017/06/03/231142
    for si in s:
        ndp = [False] * size_max

        for j in range(size_max):
            if dp[j]:
                ndp[j] = True

                if j + si < size_max:
                    ndp[j + si] = True

        dp = ndp
    
    ans = 0

    for i, di in enumerate(dp):
        if di and (i % 10 != 0):
            ans = max(ans, i)
    
    print(ans)


if __name__ == "__main__":
    main()
