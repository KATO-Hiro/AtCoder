# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n = int(input())

    # https://atcoder.jp/contests/tessoku-book/submissions/34955585
    # nが小さいので、 # 2進数に変換 + 0→4、1→7に置き換え
    n -= 1

    # ゼロ埋めも
    b = bin(n)[2:].zfill(10)
    b = b.replace("0", "4").replace("1", "7")
    print(b)


if __name__ == "__main__":
    main()
