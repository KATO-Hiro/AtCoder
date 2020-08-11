# -*- coding: utf-8 -*-


def main():
    n, m = map(int, input().split())
    s = list()
    c = list()

    for i in range(m):
        si, ci = map(int, input().split())
        si -= 1

        s.append(si)
        c.append(ci)

    # KeyInsight
    # 全探索
    # https://www.youtube.com/watch?v=TdR816rqc3s&feature=youtu.be
    # https://drken1215.hatenablog.com/entry/2020/03/02/015100
    for i in range(1000):
        digit = list(str(i))

        # 入力の桁よりも小さい
        if len(digit) != n:
            continue

        ok = True

        # 各桁で矛盾がないかチェック
        # 誤読: 同じ桁で違う数字が出てきたらNGなのに、最小の数字を選択すればいいと思っていた
        # 境界値: 先頭の桁が0がどうかの判定をifで処理したつもりになっていた
        for j in range(m):
            if int(digit[s[j]]) != c[j]:
                ok = False

        if ok:
            print(i)
            exit()

    print(-1)


if __name__ == '__main__':
    main()
