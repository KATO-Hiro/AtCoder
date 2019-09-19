# -*- coding: utf-8 -*-


def main():
    s = input()
    n = len(s)

    # KeyInsight
    # 2文字が全て同じ，もしくは，3文字のうち2文字以上が同じ文字なら
    # 条件を満たす
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            print(i + 1, i + 2)
            exit()

    for j in range(n - 2):
        if len(set(list(s[j:j + 3]))) <= 2:
            print(j + 1, j + 3)
            exit()

    print(-1, -1)


if __name__ == '__main__':
    main()
