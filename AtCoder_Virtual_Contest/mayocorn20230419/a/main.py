# -*- coding: utf-8 -*-


def f(a, b, p):
    if a > b:
        a, b = b, a

    return a < p < b


def main():
    import sys

    input = sys.stdin.readline

    x, y, z = map(int, input().split())
    ans = -1

    # 場合分け + 同じ条件をまとめる
    # 0とXの間にYはない: |X|
    # 0とXの間にYがある:
    #    0とZの間にYがある: -1 
    #    0とZの間にYはない: |z - x| + |z| 
    if f(0, x, y):
        if not f(0, z, y):
            ans = abs(z - x) + abs(z)
    else:
        ans = abs(x)

    print(ans)


if __name__ == "__main__":
    main()
