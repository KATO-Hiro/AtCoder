# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    d = 1

    # 例外処理
    if n == 1:
        print(0)
        exit()

    n -= 1

    while True:
        # 前半の桁数がdのとき、now個の回文が存在
        now = 9 * 10 ** ((d - 1) // 2)

        if n > now:
            n -= now
        else:
            # d桁のときの先頭の数は、10000...0000になっていることをnに反映させる
            # nowを利用して求める
            n += now // 9 - 1

            # 回文の構成
            former = list(str(n))
            latter = former[::-1]

            # 奇数桁のときは、真ん中の重複を除外
            if d % 2 == 1:
                former.pop()

            ans = "".join(former + latter)
            print(ans)
            exit()

        d += 1


if __name__ == "__main__":
    main()
