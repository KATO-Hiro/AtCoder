# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, k = map(int, input().split())
    size = 61
    c = [[0 for _ in range(size)] for _ in range(size)]
    c[0][0] = 1

    # nCrを前計算
    for i in range(60):
        for j in range(i + 1):
            c[i + 1][j] += c[i][j]
            c[i + 1][j + 1] += c[i][j]

    ans = ""

    while a + b > 0:
        x = 0  # 先頭の文字を固定したときの組み合わせの数

        if a >= 1:
            x = c[a - 1 + b][a - 1]

        if k <= x:
            ans += "a"
            a -= 1
        else:
            ans += "b"
            b -= 1
            k -= x  # インデックスの補正

    print(ans)


if __name__ == "__main__":
    main()
