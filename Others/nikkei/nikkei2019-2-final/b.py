# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)
    count = 0

    # S3とS4の候補を全探索
    for i in range(2, n - 2):
        for j in range(i + 1, n - 2, 2):
            center = (j - i + 1) // 2
            s3 = s[i: i + center]
            s4 = s[i + center: j + 1]

            if s3 != s4:
                continue

            # S1とS2，S5とS6の候補を列挙
            # 実装を楽にするために反転させている
            s12 = s[:i][::-1]
            s56 = s[j + 1:][::-1]

            # 先頭から共通する文字数をカウント
            for k in range(min(i, n - j - 1) - 1):
                if s12[k] == s56[k]:
                    count += 1
                else:
                    break

    print(count)


if __name__ == '__main__':
    main()
