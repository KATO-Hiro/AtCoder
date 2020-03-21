# -*- coding: utf-8 -*-


def main():
    a = int(input())
    # KeyInsight:
    # パスカルの三角形を書いてみると・・・
    # 1
    # 1 1
    # 1 2 1
    # 1 3 3 1
    # 1 4 6 4 1
    # ...

    # 制約条件下では、どの整数aもパスカルの三角形に含まれる
    # 理由: ある段iの左から2個目の数は、i - 1段目の左から2個目の数 + 1になっている
    # 出力する値がaよりも小さくなっていたら、難易度が上がっていたと思う
    print(a + 1, 2)


if __name__ == '__main__':
    main()
