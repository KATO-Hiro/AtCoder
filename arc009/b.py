# -*- coding: utf-8 -*-


def main():
    # See:
    # https://atcoder.jp/contests/arc009/submissions/6100055
    b = {int(x): index for index, x in enumerate(input().split())}

    # 再帰関数で1桁ずつ対応する数字に変換
    def f(x):
        if x < 10:
            return b[x]

        p, q = divmod(x, 10)

        return 10 * f(p) + b[q]

    n = int(input())
    words = [int(input()) for _ in range(n)]

    # 自分で作成した関数でsortできるのは知らなかった
    sorted_words = sorted(words, key=f)
    print('\n'.join(map(str, sorted_words)))


if __name__ == '__main__':
    main()
