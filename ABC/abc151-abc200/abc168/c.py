# -*- coding: utf-8 -*-


def main():
    from math import cos
    from math import pi
    from math import sqrt
    import sys
    input = sys.stdin.readline

    a, b, h, m = map(int, input().split())

    # KeyInsight:
    # 時針: h + m / 60時間で動いた角度 = 分針が動いた分も考慮する必要がある
    # 余弦定理
    hour = (60 * h + m) / 720 * 2 * pi
    minute = m / 60 * 2 * pi
    angle = abs(hour - minute)

    c = (a ** 2) + (b ** 2) - 2 * a * b * cos(angle)
    print(sqrt(c))


if __name__ == '__main__':
    main()
