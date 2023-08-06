# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))

    # 考察のステップ
    # 1. 数列の最終的な値: x, x, ..., x, x + 1, x + 1, ..., x + 1
    # xがc個、x + 1がd個あるとする（c + d = n）
    # x + 1が0個のケースもありうる

    # 2. 不変量に着目。aの総和sは、操作の前後・順番に関わらず一定。
    # s = x * c + (x + 1) * d
    #   = x * (c + d) + d
    #   = x * n + d

    # 3. xを求める
    s = sum(a)
    x, q = divmod(s, n)

    # 4. 操作後の数列をbとすると、求めたい値は|bi - ai|を最小化したもの
    # 数列a、bを昇順にソートする部分の正当性を十分理解できていない
    a = sorted(a)
    b = [x] * n

    for i in range(q):
        b[i] += 1

    b = b[::-1]

    ans = 0

    for ai, bi in zip(a, b):
        ans += abs(bi - ai)

    # print(a, b)
    print(ans // 2)


if __name__ == "__main__":
    main()
