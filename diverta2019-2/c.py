# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    plus = [a[-1]]
    minus = [a[0]]

    # KeyInsight
    # 具体的な数字ではなく，変数として扱う
    # 数列のうち，1つは正，もう一つは負として扱う
    # 残りは，正の値となるように符号を調整
    # See:
    # https://www.youtube.com/watch?v=TbobvdA6AlE
    for ai in a[1:-1]:
        if ai >= 0:
            plus.append(ai)
        else:
            minus.append(ai)

    print(sum(plus) - sum(minus))

    # 正として扱う要素を1つ以外，操作(x - y)を行う
    for p in plus[1:]:
        print(minus[-1], p)
        minus[-1] -= p

    for m in minus:
        print(plus[0], m)
        plus[0] -= m


if __name__ == '__main__':
    main()
