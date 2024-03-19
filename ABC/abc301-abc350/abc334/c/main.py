# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = [0] + [2] * n

    # 各色の個数を昇順に並べる
    for ai in a:
        count[ai] -= 1

    x = list()

    for i in range(1, n + 1):
        for _ in range(count[i]):
            x.append(i)

    # 偶奇で場合分け
    size = len(x)

    if size % 2 == 0:
        ans = 0

        for i in range(size // 2):
            ans += x[2 * i + 1] - x[2 * i]
    else:
        # 奇数番目の色を削除したときのみ考えればよい
        # 初期解: 1番目を削除
        candidate = 0

        for i in range(size // 2):
            candidate += x[2 * i + 2] - x[2 * i + 1]

        ans = candidate

        # 差分を更新
        for j in range(2, size, 2):
            candidate += x[j - 1] - x[j - 2]
            candidate -= x[j] - x[j - 1]

            ans = min(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
