# -*- coding: utf-8 -*-


# WA1個は、from math import ceilに起因しているっぽいので、自前で実装
def ceil(a, b):
    return (a + b - 1) // b


# 残り2つの長方形が領域内か?
def f2(xi, yi, ai, bi):
    width = ceil(ai, yi) + ceil(bi, yi)

    return width <= xi


# 最初の長方形を指定
def f(xi, yi, ai, bi, ci):
    width = ceil(ai, yi)

    if width >= xi:
        return False
    
    xi -= width

    return f2(xi, yi, bi, ci) or f2(yi, xi, bi, ci)


def main():
    import sys

    input = sys.stdin.readline

    x, y, a, b, c = map(int, input().split())

    # 長方形の4パターンを試す
    # 対称性を利用 = swapすることで、場合分けを減らす
    for i in range(2):
        for j in range(3):
            if f(x, y, a, b, c):
                print("Yes")
                exit()

            b, c, a = a, b, c
        
        x, y = y, x
    
    print("No")


if __name__ == "__main__":
    main()
