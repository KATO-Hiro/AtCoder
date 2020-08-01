# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = sorted(list(map(int, input().split())))

    # KeyInsights:
    # ◯: ペアを組む: 強さの値が大きい人と小さい人
    # △: ペア同士の比較: aを昇順で並び替えたときの両端と真ん中のペアだと思い込んでいた
    #    制約条件から愚直に比較するは十分にできる

    # See:
    # https://atcoder.jp/contests/indeednow-finala-open/submissions/7076305
    pairs = [i + j for i, j in zip(a, a[::-1])]
    print(max(pairs) - min(pairs))


if __name__ == '__main__':
    main()
