# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    # x, y軸への操作を独立に考えると良さそう
    # 回転の角度・方向が決まっているので、aとの関連付けができるはず
    # 移動距離ai = 各軸方向へ1倍 or -1倍
    # 各軸について移動したときに、x、yの位置にいられるか? = 部分和問題っぽい
    # 部分和問題 = DP
    x_axis = a[::2]
    y_axis = a[1::2]
    # print(x_axis, y_axis)

    base = 10**4
    size = 2 * base + 1
    dp_x = [False] * size
    dp_y = [False] * size
    dp_x[base], dp_y[base] = True, True

    def f(axis, dp, is_x):
        for i, axis_i in enumerate(axis):
            ndp = [False] * size

            for j in range(size):
                if not dp[j]:
                    continue

                if (j - axis_i >= 0) and not (is_x and i == 0):
                    ndp[j - axis_i] = True
                if j + axis_i < size:
                    ndp[j + axis_i] = True

            dp = ndp

        return dp

    results_x = f(x_axis, dp_x, True)
    results_y = f(y_axis, dp_y, False)

    if results_x[x + base] and results_y[y + base]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
