# -*- coding: utf-8 -*-


def main():
    import sys
    from itertools import permutations

    input = sys.stdin.readline

    cells = list()

    # グリッドを1次元にすることで、順列との対応づけがしやすくなる
    for _ in range(3):
        ci = list(map(int, input().split()))
        cells += ci

    # print(cells)

    # 縦・横・斜めのマス(0-8)の組を用意
    trio = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (2, 4, 6),
        (0, 4, 8),
    ]

    count, count_all = 0, 0

    for order in permutations(range(9)):
        count_all += 1
        ok = True

        # がっかり = 最初の2つが同じ数字で、3つ目の数字が最後に登場
        # ペアが3種類
        for a, b, c in trio:
            if (
                (cells[a] == cells[b])
                and (order[a] < order[c])
                and (order[b] < order[c])
            ):
                ok = False
                break

            if (
                (cells[b] == cells[c])
                and (order[b] < order[a])
                and (order[c] < order[a])
            ):
                ok = False
                break

            if (
                (cells[c] == cells[a])
                and (order[c] < order[b])
                and (order[a] < order[b])
            ):
                ok = False
                break

        if ok:
            count += 1

    print(count / count_all)


if __name__ == "__main__":
    main()
