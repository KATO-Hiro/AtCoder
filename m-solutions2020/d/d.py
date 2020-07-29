# -*- coding: utf-8 -*-


def main():
    import sys
    input = sys.stdin.readline

    n = int(input())
    a = list(map(int, input().split()))
    money = 1000

    # 反省点:
    # 難しく考えすぎて、実装しきれなかった。
    # ある時点で最も安い値のときに買って、最も高いときに売る、という考え方をしていた。
    # 「何もしない」「買う」「売る」の3パターンを愚直に遷移させようとしていた。

    # KeyInsight:
    # 「i日目には、その時点で所持する金と株の範囲内で、M君は次の取引を何回でも行えます。」を、
    # = i日目の最初に全て売る + 必要に応じて買い戻す と言い換える。
    # See:
    # https://www.youtube.com/watch?v=z6SeLXdwVhA&feature=youtu.be

    for i in range(n - 1):
        today = a[i]
        tomorrow = a[i + 1]

        if tomorrow > today:
            count = money // today
            money %= today
            money += tomorrow * count

    print(money)


if __name__ == '__main__':
    main()
