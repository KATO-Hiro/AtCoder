# -*- coding: utf-8 -*-


def main():
    import sys
    from string import ascii_uppercase

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    alpha = ascii_uppercase
    alpha_count = len(ascii_uppercase)

    # 3要素のうち真ん中を固定
    # 文字は26種類なので、前計算で左から累積和を取る
    acc_from_left = [[0] * n for _ in range(alpha_count)]

    for i, a in enumerate(alpha):
        for j, si in enumerate(s):
            if j >= 1:
                acc_from_left[i][j] = acc_from_left[i][j - 1]

            if si == a:
                acc_from_left[i][j] += 1

    ans = 0

    for j in range(1, n - 1):
        for i in range(alpha_count):
            left = acc_from_left[i][j - 1]
            right = acc_from_left[i][n - 1] - acc_from_left[i][j]

            ans += left * right

    print(ans)


if __name__ == "__main__":
    main()
