# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    _, c = input().rstrip().split()
    s = input().rstrip()

    # 白: 0、青: 1、赤: 2と番号を振り、それらの合計をスコアとする
    # スコア mod 3は、6種類の操作により変化しない
    # どうしたら思いつける? or 典型的なテクニック?
    colors = {"W": 0, "B": 1, "R": 2}
    scores = 0

    for si in s:
        scores += colors[si]

    if scores % 3 == colors[c]:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
