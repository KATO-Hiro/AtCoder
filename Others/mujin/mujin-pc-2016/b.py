# -*- coding: utf-8 -*-


def main():
    from math import pi
    import sys
    input = sys.stdin.readline

    oa, ab, bc = map(int, input().split())
    large_r = oa + ab + bc
    longest = max(oa, ab, bc)
    shortest = min(oa, ab, bc)
    middle = large_r - (longest + shortest)

    # See:
    # https://www.slideshare.net/chokudai/mujin2016
    if shortest + middle >= longest:
        # 三角形が作れるため、原点と点Cが一致する
        small_r = 0
    else:
        # 線分OA, AB, BCを入れ替えても、点Cの座標は変わらない
        small_r = longest - (shortest + middle)

    print(((large_r ** 2) - (small_r ** 2)) * pi)


if __name__ == '__main__':
    main()
