# -*- coding: utf-8 -*-


def f(number) -> int:
    return number + digit_sum(number)


def digit_sum(number: int) -> int:
    return sum(map(int, list(str(number))))


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # dp[i]: 整数iに対して0回以上操作を行ったときに整数nにできるか?
    dp = [False] * (n + 100)
    dp[n] = True

    for i in range(n - 1, 0, -1):
        if dp[f(i)]:
            dp[i] = True

    print(sum(dp))


if __name__ == "__main__":
    main()
