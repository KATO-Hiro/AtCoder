# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, k = map(int, input().split())
    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))
    ans = -float("inf")

    # 開始位置を全探索[0, n)
    for si in range(n):
        scores = list()
        score_total = 0
        pos = si

        # 開始位置をsiとしたときの周期を検出
        while True:
            pos = p[pos]
            scores.append(c[pos])
            score_total += c[pos]

            if pos == si:
                break

        cycle_size = len(scores)
        sub_total = 0  # サイクルの途中までの合計値

        # 1サイクルのうち、最大値を求める[0, cycle_size)
        for j in range(cycle_size):
            if j + 1 > k:
                break

            sub_total += scores[j]
            # sub_totalを現在の1サイクルの最大値とする
            candidate = sub_total

            # 位置jまでの合計値を求める
            if score_total > 0:
                cycle_count = (k - (j + 1)) // cycle_size
                candidate += score_total * cycle_count

            ans = max(ans, candidate)

    print(ans)


if __name__ == "__main__":
    main()
