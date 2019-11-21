# -*- coding: utf-8 -*-


def main():
    x, y = map(int, input().split())
    n = int(input())
    xs = [0 for _ in range(n + 1)]
    ys = [0 for _ in range(n + 1)]

    for i in range(n):
        xi, yi = map(int, input().split())
        xs[i] = xi
        ys[i] = yi

    # 配列外参照をなくすための工夫
    xs[n] = xs[0]
    ys[n] = ys[0]

    ans = float('inf')

    # 隣り合う2点の直線y = ax + cを求める
    for i in range(n):
        xi = xs[i]
        xii = xs[i + 1]
        yi = ys[i]
        yii = ys[i + 1]

        # 分母が0になるときは，傾きaを計算しない
        if xii - xi == 0:
            continue

        a = (yii - yi) / (xii - xi)
        c = yi - a * xi

        # 点と直線の距離
        # See:
        # https://mathtrain.jp/tentotyokusen
        dist = abs(a * x - y + c) / (a ** 2 + (-1) ** 2) ** 0.5
        ans = min(ans, dist)

    print(ans)


if __name__ == '__main__':
    main()
