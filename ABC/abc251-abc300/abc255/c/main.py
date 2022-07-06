# -*- coding: utf-8 -*-


def f(a, n, d, i):
    # 範囲外を処理
    if i < 0:
        i = 0
    elif i >= n:
        i = n - 1

    return (a + i * d)


def main():
    import sys

    input = sys.stdin.readline

    x, a, d, n = map(int, input().split())

    if d == 0:
        print(abs(x - a))
        exit()
    
    # 例外処理: 等差数列を反転させることで扱いやすく
    if d < 0:
        a = a + (n - 1) * d
        d = -d
    
    i = (x - a) // d
    ans = abs(f(a, n, d, i) - x)
    ans = min(ans, abs(f(a, n, d, i + 1) - x))
    
    print(ans)


if __name__ == "__main__":
    main()
