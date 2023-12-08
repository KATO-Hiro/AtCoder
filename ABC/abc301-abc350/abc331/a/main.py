# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    m, d = map(int, input().split())
    y0, m0, d0 = map(int, input().split())

    # 年末、月末、それ以外
    if m0 == m and d0 == d:
        print(y0 + 1, 1, 1)
    elif d0 == d:
        print(y0, m0 + 1, 1)
    else:
        print(y0, m0, d0 + 1)


if __name__ == "__main__":
    main()
