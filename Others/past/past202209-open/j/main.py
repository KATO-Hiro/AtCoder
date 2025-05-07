# -*- coding: utf-8 -*-


def main():
    import sys
    from math import acos, cos, pi, sin

    input = sys.stdin.readline

    h, w, d = map(int, input().split())

    def calc(h, w, d):
        # 円が長方形を完全に内包 = 長方形の対角線よりも円の直径が大きい
        if (4 * d**2) >= (h**2 + w**2):
            return 1

        circle = d**2 * pi
        rect = h * w

        # 円の一部が長方形からはみ出す
        # 上下
        h_half = h / 2

        if d >= h_half:
            theta1 = acos(h_half / d)
            fan1 = theta1 * (d**2) / 2
            triangle1 = (d**2) * sin(theta1) * cos(theta1) / 2

            circle -= (fan1 - triangle1) * 4

        # 左右
        w_half = w / 2

        if d >= w_half:
            theta2 = acos(w_half / d)
            fan2 = theta2 * (d**2) / 2
            triangle2 = (d**2) * sin(theta2) * cos(theta2) / 2

            circle -= (fan2 - triangle2) * 4

        return circle / rect

    ans = calc(h, w, d)
    print("{:.10f}".format(ans))


if __name__ == "__main__":
    main()
