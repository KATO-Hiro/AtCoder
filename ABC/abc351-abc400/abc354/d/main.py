# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    # 全ての頂点が第1象限にあるようにする
    a, b, c, d = map(lambda x: int(x) + 10**9, input().split())

    # f(0, 0, x, y): 原点と(x, y)における面積を求める問題に分解 + 二次元累積和の考え方で全体の面積を求める
    def f(x, y):
        s = [[0, 0, 0, 0, 0], [0, 2, 3, 3, 4], [0, 3, 6, 7, 8]]

        p1, q1 = divmod(x, 4)
        p2, q2 = divmod(y, 2)

        # 2 * 4マスで敷き詰められる領域と、それ以外に分ける
        result = p1 * p2 * s[2][4]
        result += p1 * q2 * s[1][4]
        result += p2 * s[2][q1]
        result += q2 * s[1][q1]

        return result

    ans = f(c, d) - f(a, d) - f(c, b) + f(a, b)
    print(ans)


if __name__ == "__main__":
    main()
