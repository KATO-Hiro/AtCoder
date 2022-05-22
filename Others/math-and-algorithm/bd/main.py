# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, large_k = map(int, input().split())

    # kが小さいことをうまく利用できないか?
    # 全パターン - 条件を満たさない
    ans = n ** 3

    # See:
    # https://atcoder.jp/contests/math-and-algorithm/submissions/28585640
    # ◯: iのみ全探索
    # △: j, kの上下限を指定
    # △: abs(i - m ) < large_kのときだけチェックすればよい
    for i in range(1, n + 1):
        smallest = max(1, i - large_k + 1)
        largest = min(n + 1, i + large_k)

        for j in range(smallest, largest):
            for k in range(smallest, largest):
                if abs(j - k) < large_k:
                    ans -= 1
    
    print(ans)


if __name__ == "__main__":
    main()
