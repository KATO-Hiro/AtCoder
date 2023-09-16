# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    ac = list()
    summed = 0

    # 高橋氏が演説して得られる票数 = 青木氏が失う票数 + 高橋氏が演説して直接得られる票数
    # ゲームで相手の失点 = 自分の得点と考えると思いつきやすいか?
    # ai + (ai + bi) = 2 * ai + bi
    for _ in range(n):
        ai, bi = map(int, input().split())
        ac.append(2 * ai + bi)
        summed -= ai  # 高橋氏が失うと捉える

    ac.sort(reverse=True)
    count = 0

    while summed <= 0:
        summed += ac[count]
        count += 1

    print(count)


if __name__ == "__main__":
    main()
