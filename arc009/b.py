# -*- coding: utf-8 -*-


def main():
    from string import ascii_lowercase

    b = list(map(int, input().split()))
    n = int(input())

    # 数字をアルファベットに変換
    d = dict()
    alpha = ascii_lowercase[:len(b)]

    for index, bi in enumerate(b):
        d[bi] = alpha[index]

    ans = list()

    for _ in range(n):
        ai = input()
        mod_ai = ''

        for aii in list(ai):
            mod_ai += d[int(aii)]

        # 文字の長さ，変換後の文字列，変換前の数字
        ans.append((len(ai), mod_ai, ai))

    # 昇順に
    for _, _, number in sorted(ans):
        print(number)


if __name__ == '__main__':
    main()
