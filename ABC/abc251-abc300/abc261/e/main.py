# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, c = map(int, input().split())
    f = [0, ~0]

    # bit演算は、桁ごとに独立して考えることができる
    # {0, 1} → {0, 1}の問題に帰着できるので、関数合成を行う
    for i in range(n):
        ti, ai = map(int, input().split())

        # fi(x)が0 / 1から始まる場合の合成関数を考える
        for j in range(2):
            if ti == 1:
                f[j] &= ai
            elif ti == 2:
                f[j] |= ai
            elif ti == 3:
                f[j] ^= ai
        
        # bitごとに0 / 1でどちらの値を採用するか判定して、合成
        c = c & f[1] | (~c) & f[0]
        print(c)


if __name__ == "__main__":
    main()
