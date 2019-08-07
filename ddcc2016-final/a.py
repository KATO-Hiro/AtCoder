# -*- coding: utf-8 -*-


def main():
    r, c = map(int, input().split())
    ans = 0

    # 半径Rの円に正方形がいくつ含まれるかを数える
    # 第1象限のみを計算
    for i in range(r // c):
        for j in range(r // c):
            count = 0

            # 正方形の4点が半径Rの円の内側（円周上も含む）にあるかどうか
            for x in [0, 1]:
                for y in [0, 1]:
                    dist = ((i + x) * c) ** 2 + ((j + y) * c) ** 2

                    # 誤差の回避するため，整数同士で比較
                    if r ** 2 >= dist:
                        count += 1

            if count == 4:
                ans += 1

    # 図形の対称性から第2～4象限の正方形の個数は，第1象限の結果と同じ
    print(ans * 4)


if __name__ == '__main__':
    main()
