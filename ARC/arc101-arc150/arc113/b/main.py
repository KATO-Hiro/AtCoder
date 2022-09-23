# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c = map(int, input().split())
    d = pow(b, c, 4)  # 周期性に着目

    # 例外処理
    if d == 0:
        d = 4

    ans = pow(a, d, 10)
    print(ans)


if __name__ == "__main__":
    main()
