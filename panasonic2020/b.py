# -*- coding: utf-8 -*-


def main():
    from math import ceil
    import sys
    input = sys.stdin.readline

    h, w = map(int, input().split())

    # 境界値
    if h == 1 or w == 1:
        print(1)
        exit()

    ans = h // 2 * w

    if h % 2 == 1:
        ans += ceil(w / 2)

    print(ans)


if __name__ == '__main__':
    main()
