# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # 末尾が0 = 10の倍数
    # (2 ** x) * (5 ** y)となっているはず
    # xの個数 >> yの個数
    # yを高速に数えたい
    if n % 2 == 1:
        ans = 0
    else:
        # 10の倍数 + 5の倍数がどれだけ含まれているか?
        ans = n // 10
        five = 10

        while five <= n:
            five *= 5
            ans += n // five

    print(ans)


if __name__ == "__main__":
    main()
