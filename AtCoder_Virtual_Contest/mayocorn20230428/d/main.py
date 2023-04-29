# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    if n % 2 == 1:
        print(0)
        exit()

    # 10の倍数がいくつあるか?
    ans = n // 10
    n //= 10

    # 10の倍数のうち、min(2の倍数, 5の倍数)
    # 2の倍数はたくさんあるので、5の倍数だけに着目すると良い
    pow_5 = 5

    while pow_5 <= n:
        ans += n // pow_5
        pow_5 *= 5

    print(ans)


if __name__ == "__main__":
    main()
