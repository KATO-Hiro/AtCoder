# -*- coding: utf-8 -*-


def main():
    import sys
    from string import ascii_uppercase

    input = sys.stdin.readline

    s = input().rstrip()
    t = s[::-1]
    n = len(s)
    alpha = ascii_uppercase
    alpha_count = len(ascii_uppercase)

    # 3要素のうち真ん中を固定
    # 文字は26種類なので、前計算で左右から累積和を取る
    acc_from_left = [[0] * n for _ in range(alpha_count)]
    acc_from_right = [[0] * n for _ in range(alpha_count)]

    for i, a in enumerate(alpha):
        for j, si in enumerate(s):
            if j >= 1:
                acc_from_left[i][j] = acc_from_left[i][j - 1]

            if si == a:
                acc_from_left[i][j] += 1

    for i, a in enumerate(alpha):
        for j, ti in enumerate(t):
            if j >= 1:
                acc_from_right[i][j] = acc_from_right[i][j - 1]

            if ti == a:
                acc_from_right[i][j] += 1

        acc_from_right[i] = acc_from_right[i][::-1]

    ans = 0

    for j in range(1, n - 1):
        for i in range(alpha_count):
            ans += acc_from_left[i][j - 1] * acc_from_right[i][j + 1]

    print(ans)


if __name__ == "__main__":
    main()
