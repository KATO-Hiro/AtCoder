# -*- coding: utf-8 -*-


def euclidean_distance_2d(a, b, theta_a, theta_b):
    from math import hypot, cos, sin, radians

    x_a, y_a = a * cos(radians(theta_a)), a * sin(radians(theta_a))
    x_b, y_b = b * cos(radians(theta_b)), b * sin(radians(theta_b))

    return hypot(x_a - x_b, y_a - y_b)


def main():
    import sys

    input = sys.stdin.readline

    a, b, h, m = map(int, input().split())
    theta_a = (h * 60 + m) * 360 / 720
    theta_b = m * 360 / 60
    ans = euclidean_distance_2d(a, b, theta_a, theta_b)
    print(ans)


if __name__ == "__main__":
    main()
