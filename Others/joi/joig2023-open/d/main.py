# -*- coding: utf-8 -*-


def main():
    import sys
    from copy import deepcopy

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    counts = [0] * w

    # 各列の表向きのコインの枚数を数える
    for j in range(w):
        for i in range(h):
            if s[i][j] == "#":
                counts[j] += 1

    # print(counts)
    first_max = 0

    # 各行を反転させ、後手が最善手を取ったときの両者のコインの枚数をシミュレーション
    for i in range(h):
        cur_counts = deepcopy(counts)

        for j in range(w):
            if s[i][j] == "#":
                cur_counts[j] -= 1
            else:
                cur_counts[j] += 1

        # 後手の最善手による結果を反映(表→裏、裏→表)
        first = sum(cur_counts) - max(cur_counts) + (h - max(cur_counts))
        first_max = max(first_max, first)

    print(first_max, h * w - first_max)


if __name__ == "__main__":
    main()
