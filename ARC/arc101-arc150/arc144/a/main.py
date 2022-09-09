# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # 桁和と繰り上がり回数kの関係
    # f(a + b) = f(a) + f(b) - 9k
    # 繰り上がりが発生するとある桁が-10、一つ上の桁が+1になるため

    # m:
    # f(2x) = f(x + x) = f(x) + f(x) - 9k = 2n - 9k
    # Mを最大化するには、-9kが0だと嬉しい
    # 桁の繰り上がりが発生しないのは、各桁とも4以下の場合
    # f(2x) = 2n = m
    m = 2 * n

    # x:
    # できるだけ桁数を少なく = 利用できる数のうち最大の値を使うと良さそう
    # 基本的には4で埋める
    # mod 4で余りが0以外のときは、先頭にその余りをつけると良さそう
    p, q = divmod(n, 4)
    x = '4' * p

    if q != 0:
        x = str(q) + x
    
    print(m)
    print(x)


if __name__ == "__main__":
    main()
