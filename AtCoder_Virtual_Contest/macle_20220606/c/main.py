# -*- coding: utf-8 -*-


def g(x):
    return x * (x + 1) // 2


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ans = 0

    # 約数を並べると、iの倍数になっている
    # 1の倍数の和を高速に求める g(n) = n * (n + 1) // 2
    # 2の倍数の和は、g(n // 2)
    for i in range(1, n + 1):
        ans += i * g(n // i)

    print(ans)


if __name__ == "__main__":
    main()
