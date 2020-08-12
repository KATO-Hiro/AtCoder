# -*- coding: utf-8 -*-


def main():
    h, w = map(int, input().split())
    alpha = [0 for _ in range(26)]

    # 各アルファベットの個数を数える
    for i in range(h):
        ai = list(input())

        for aii in ai:
            # アルファベットを数値に変換
            index = ord(aii) - ord('a')
            alpha[index] += 1

    mod = [0 for _ in range(4)]

    for a in alpha:
        mod[a % 4] += 1

    # 回文となる条件
    # 1. hとwがともに偶数：
    # アルファベットの個数が全て4の倍数のとき，Yes
    # 2. hとwのどちらかが偶数：
    # アルファベットの個数が全て2の倍数のとき，Yes
    # 3. hとwがともに奇数：
    # (h - 1) * (w - 1)マス分，アルファベットの個数が4の倍数であり，
    # かつ，1種類を除いて，2の倍数のとき，Yes
    if h % 2 == 0 and w % 2 == 0:
        for a in alpha:
            if a % 4 != 0:
                print('No')
                exit()

        print('Yes')
    elif h % 2 == 1 and w % 2 == 1:
        # 気がつけなかった点
        # 4で割ったときに2余る数が使われるのが，(h - 1) // 2 + (w - 1) // 2以下
        # See:
        # https://www.hamayanhamayan.com/entry/2017/09/24/012523
        if mod[3]:
            print('No')
        elif mod[1] != 1:
            print('No')
        elif mod[2] > ((h - 1) // 2 + (w - 1) // 2):
            print('No')
        else:
            print('Yes')
    else:
        if w % 2 == 1:
            h, w = w, h

        # 気がつけなかった点
        if mod[3] or mod[1]:
            print('No')
        elif mod[2] > w // 2:
            print('No')
        else:
            print('Yes')


if __name__ == '__main__':
    main()
