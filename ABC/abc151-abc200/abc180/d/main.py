# -*- coding: utf-8 -*-


def main():
    x, y, a, b = map(int, input().split())
    ans = 0

    # See:
    # https://www.youtube.com/watch?v=r4ujcFBDBw4&feature=youtu.be
    # コーナーケースにハマった
    if a < b:
        # 問題文から得られる情報をもとに、条件式を丁寧に書き出す
        while (x * a < x + b) and (x * a < y):
            x *= a
            ans += 1

    # y未満となるように-1する
    ans += (y - x - 1) // b

    print(ans)


if __name__ == "__main__":
    main()
