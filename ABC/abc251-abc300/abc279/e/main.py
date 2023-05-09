# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    a = list(map(lambda x: int(x) - 1, input().split()))

    # あみだくじから横線1本を取り除く問題と捉える
    # 1. 上側から1の位置を前計算
    s = [0] * m
    pos = 0

    for i in range(m):
        s[i] = pos

        # swapにより1が移動
        if pos == a[i]:
            pos += 1
        elif pos == a[i] + 1:
            pos -= 1

    # 2. 下側からシミュレーション
    b = [i for i in range(1, n + 1)]
    ans = [0] * m

    for j in range(m - 1, -1, -1):
        ans[j] = b[s[j]]

        # swap
        b[a[j]], b[a[j] + 1] = b[a[j] + 1], b[a[j]]

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
