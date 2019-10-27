# -*- coding: utf-8 -*-


def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 1
    ans = 0

    # KeyInsight
    # 単調増加する数列の個数mを数える
    # m * (m + 1) // 2個がl, rの組み合わせの数
    for i in range(1, n):
        if a[i] > a[i - 1]:
            count += 1
        else:
            ans += count * (count + 1) // 2
            count = 1

    ans += count * (count + 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
