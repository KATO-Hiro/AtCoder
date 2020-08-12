# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0

    # KeyInsight
    # 左側の桁から順番にmodを取る
    # 新しい桁を見るときは，その桁数の分だけずらす
    # See:
    # https://atcoder.jp/contests/chokudai_S001/submissions/1458821
    for i in range(n):
        ans = ans * 10 ** len(str(a[i])) + a[i]
        ans %= mod

    print(ans)


if __name__ == '__main__':
    main()
