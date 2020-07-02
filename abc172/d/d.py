# -*- coding: utf-8 -*-


def g(x):
    return x * (x + 1) // 2


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    ans = 0

    # See: https://www.youtube.com/watch?v=v8ppNGf49Nk&feature=youtu.be
    # KeyInsight:
    # ①約数⇄倍数と言い換え
    # 1の倍数: 1, 2, 3, 4, 5, 6, 7, 8, 9, ...
    # 2の倍数: 2, 4, 6, 8, ...
    # 3の倍数: 3, 6, ...
    # ...

    # ②1の倍数の和を基準に、等価な式変形を行う
    # 1の倍数の和は、g(x) = n * (n + 1) // 2
    # 2の倍数の和は、2 * (1, 2, 3, 4, ...)と考えることで、 2 * g(x / 2)
    # 以降、同様

    for i in range(1, n + 1):
        ans += i * g(n // i)

    print(ans)


if __name__ == '__main__':
    main()
