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
    x_axis = a[2::2]  # 1回目の移動は必ず正なので、除外
    y_axis = a[1::2]
    dp_x = set([a[0]])
    dp_y = set([0])

    def f(dp, axis):
        for axis_i in axis:
            ndp = set()

            for dp_i in dp:
                ndp.add(dp_i - axis_i)
                ndp.add(dp_i + axis_i)

            dp = ndp

        return dp

    results_x = f(dp_x, x_axis)
    results_y = f(dp_y, y_axis)

    if x in results_x and y in results_y:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
